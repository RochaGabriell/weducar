from rest_framework import serializers

from ..models import Color


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if 'description' in representation and representation['description']:
            representation['description'] = representation['description'].upper()
        return representation
