from rest_framework import serializers

from ..models import JustifiedAbsence


class JustifiedAbsenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = JustifiedAbsence
        fields = '__all__'
