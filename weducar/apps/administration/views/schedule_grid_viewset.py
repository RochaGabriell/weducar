from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions

from ..serializers.schedule_grid_serializer import ScheduleGridSerializer
from ..models import ScheduleGrid


class ScheduleGridViewSet(viewsets.ModelViewSet):
    queryset = ScheduleGrid.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ScheduleGridSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
