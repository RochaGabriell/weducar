from rest_framework import serializers

from ..models import Schooling


class SchoolingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schooling
        fields = "__all__"
