from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import ValidationError
from rest_framework import viewsets, permissions
from rest_framework.response import Response

from ..serializers.student_serializer import StudentSerializer, StudentDetailSerializer
from ..models import Student


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['name']
    ordering_fields = ['name']
    filterset_fields = ['student_status_id', 'instance_id']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return StudentDetailSerializer
        return StudentSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.request.user.is_authenticated:
            instance_id = self.request.query_params.get('instance_id')

            if not instance_id and not self.request.user.is_superuser:
                raise ValidationError(
                    {"error": "A Instância deve ser informada para este usuário."}
                )

            queryset = self.queryset
            if instance_id:
                queryset = queryset.filter(instance_id=instance_id)

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)

        serializer = self.get_serializer(page, many=True)
        paginated_response = self.get_paginated_response(serializer.data)

        paginated_response.data['filters'] = {
            "search_fields": self.search_fields,
            "ordering_fields": self.ordering_fields,
            "filterset_fields": self.filterset_fields,
        }

        return paginated_response
