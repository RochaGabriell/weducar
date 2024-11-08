from rest_framework import serializers

from ..models import StudentStatus


class StudentStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentStatus
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if 'description' in representation and representation['description']:
            representation['description'] = representation['description'].upper()
        return representation
