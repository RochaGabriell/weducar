from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions

from ..serializers.employee_school_serializer import EmployeeSchoolSerializer
from ..models import EmployeeSchool


class EmployeeSchoolViewSet(viewsets.ModelViewSet):
    queryset = EmployeeSchool.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EmployeeSchoolSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
