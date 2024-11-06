from rest_framework import viewsets, permissions

from ..serializers.color_serializer import ColorSerializer
from ..models import Color


class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    permission_classes = [permissions.IsAuthenticated]
