from rest_framework import serializers

from ..models import LessonContent


class LessonContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonContent
        fields = '__all__'
