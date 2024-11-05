from rest_framework import serializers

from weducar.apps.administration.serializers import EmployeeSerializer
from ..models import User


class UserSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()
    schools = serializers.SerializerMethodField()
    instances = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'username',
            'access_count',
            'last_access',
            'is_active',
            'is_staff',
            'is_superuser',
            'employee',
            'schools',
            'instances',
        ]

        extra_kwargs = {'password': {'write_only': True}}

    def get_schools(self, obj):
        return obj.get_schools()

    def get_instances(self, obj):
        return obj.get_instances()


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'employee'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
