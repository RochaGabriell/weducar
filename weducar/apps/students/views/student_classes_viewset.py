from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions

from ..serializers.student_classes_serializer import StudentClassesSerializer
from ..models import StudentClasses


class StudentClassesViewSet(viewsets.ModelViewSet):
    queryset = StudentClasses.objects.all()
    serializer_class = StudentClassesSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    def get_queryset(self):
        student_id = self.kwargs.get('student_id')
        return StudentClasses.objects.filter(student_enrollment__registration=student_id)
