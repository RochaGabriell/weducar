from rest_framework import serializers

from ..models import HistoryArea


class HistoryAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryArea
        fields = '__all__'
