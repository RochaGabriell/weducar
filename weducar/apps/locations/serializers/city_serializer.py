from rest_framework import serializers

from ..models import City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if 'name' in representation and representation['name']:
            representation['name'] = representation['name'].upper()
        return representation
