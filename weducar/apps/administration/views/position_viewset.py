from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions

from ..serializers.position_serializer import PositionSerializer
from ..models import Position


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PositionSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
