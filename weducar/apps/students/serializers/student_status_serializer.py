from rest_framework import serializers

from ..models import StudentStatus


class StudentStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentStatus
        fields = '__all__'
