from rest_framework import serializers

from weducar.apps.locations.serializers import CitySerializer, HousingSerializer, InstanceSerializer
from ..serializers.student_status_serializer import StudentStatusSerializer
from ..models import Student


class StudentSerializer(serializers.ModelSerializer):
    classe = serializers.SerializerMethodField()
    student_status_id = StudentStatusSerializer()

    class Meta:
        model = Student
        fields = [
            'registration',
            'name',
            'responsible_name',
            'classe',
            'student_status_id',
        ]

    def get_classe(self, obj):
        return obj.get_classe()


class StudentDetailSerializer(serializers.ModelSerializer):
    student_status_id = StudentStatusSerializer()
    city_id = CitySerializer()
    instance_id = InstanceSerializer()
    housing_id = HousingSerializer()

    class Meta:
        model = Student
        fields = '__all__'
