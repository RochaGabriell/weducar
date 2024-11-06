from rest_framework import serializers

from weducar.apps.locations.serializers import CitySerializer, HousingSerializer, InstanceSerializer
from ..serializers.student_status_serializer import StudentStatusSerializer
from ..serializers.color_serializer import ColorSerializer
from ..models import Student


class StudentSerializer(serializers.ModelSerializer):
    classe = serializers.SerializerMethodField()
    color_obj = ColorSerializer(source='color', read_only=True)
    student_status_obj = StudentStatusSerializer(
        source='student_status', read_only=True
    )

    class Meta:
        model = Student
        fields = [
            'registration',
            'census_id',
            'name',
            'gender',
            'color',
            'color_obj',
            'birth_date',
            'father_name',
            'father_phone',
            'father_rg',
            'father_cpf',
            'mother_name',
            'mother_phone',
            'mother_rg',
            'mother_cpf',
            'responsible_relationship',
            'responsible_name',
            'responsible_phone',
            'responsible_rg',
            'responsible_cpf',
            'address',
            'neighborhood',
            'allergy_check',
            'allergy_observations',
            'medical_monitoring_check',
            'medical_monitoring_observations',
            'physical_activity_restriction_check',
            'physical_activity_restriction_observations',
            'disorder_check',
            'disorder_observations',
            'disorder_instructions',
            'medication_check',
            'medication_observations',
            'food_restriction_check',
            'food_restriction_observations',
            'image_right_check',
            'sus_number',
            'nis_number',
            'old_birth_certificate_check',
            'birth_certificate',
            'birth_certificate_issue_date',
            'birth_certificate_registry',
            'birthplace',
            'rg',
            'cpf',
            'school_transport_check',
            'disability_check',
            'disability_observations',
            'aee_check',
            'photo',
            'date_joined',
            'date_changed',
            'classe',
            'student_status',
            'student_status_obj',
            'city',
            'instance',
            'housing'
        ]

    def get_classe(self, obj):
        return obj.get_classe()

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        fields_to_uppercase = [
            'name', 'father_name', 'mother_name',
            'responsible_relationship', 'responsible_name'
        ]

        for field in fields_to_uppercase:
            if field in representation and representation[field]:
                representation[field] = representation[field].upper()

        return representation


class StudentDetailSerializer(serializers.ModelSerializer):
    student_status = StudentStatusSerializer()
    city = CitySerializer()
    instance = InstanceSerializer()
    housing = HousingSerializer()
    color = ColorSerializer()

    class Meta:
        model = Student
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        fields_to_uppercase = [
            'name', 'father_name', 'mother_name',
            'responsible_relationship', 'responsible_name'
        ]

        for field in fields_to_uppercase:
            if field in representation and representation[field]:
                representation[field] = representation[field].upper()

        return representation
