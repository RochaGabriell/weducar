from rest_framework import serializers

from ..models import CurricularComponent


class CurricularComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurricularComponent
        fields = '__all__'
