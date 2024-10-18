from rest_framework import serializers

from ..models import SysPresence


class SysPresenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SysPresence
        fields = '__all__'
