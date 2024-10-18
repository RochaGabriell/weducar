from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions

from ..serializers.sys_presence_serializer import SysPresenceSerializer
from ..models import SysPresence


class SysPresenceViewSet(viewsets.ModelViewSet):
    queryset = SysPresence.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SysPresenceSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
