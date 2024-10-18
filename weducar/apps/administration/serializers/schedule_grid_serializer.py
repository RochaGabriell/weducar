from rest_framework import serializers

from ..models import ScheduleGrid


class ScheduleGridSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleGrid
        fields = '__all__'
