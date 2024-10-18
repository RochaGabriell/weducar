from rest_framework import serializers

from ..serializers.schooling_serializer import SchoolingSerializer
from ..models import Employee


class EmployeeSerializer(serializers.ModelSerializer):

    schooling = SchoolingSerializer()

    class Meta:
        model = Employee
        fields = "__all__"
