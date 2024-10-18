from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions

from ..serializers.history_area_serializer import HistoryAreaSerializer
from ..models import HistoryArea


class HistoryAreaViewSet(viewsets.ModelViewSet):
    queryset = HistoryArea.objects.all()
    serializer_class = HistoryAreaSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
