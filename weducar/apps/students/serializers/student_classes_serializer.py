from rest_framework import serializers

from ..models import StudentClasses


class StudentClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentClasses
        fields = '__all__'
