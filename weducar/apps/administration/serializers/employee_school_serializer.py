from rest_framework import serializers

from ..models import EmployeeSchool


class EmployeeSchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeSchool
        fields = '__all__'