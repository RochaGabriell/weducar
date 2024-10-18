from rest_framework import serializers

from ..models import CurricularComponentMatrix


class CurricularComponentMatrixSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurricularComponentMatrix
        fields = '__all__'
