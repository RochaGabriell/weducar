from rest_framework import serializers

from ..models import CurricularMatrix


class CurricularMatrixSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurricularMatrix
        fields = '__all__'
