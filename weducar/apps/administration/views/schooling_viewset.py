from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions

from ..serializers.schooling_serializer import SchoolingSerializer
from ..models import Schooling


class SchoolingViewSet(viewsets.ModelViewSet):
    queryset = Schooling.objects.all()
    serializer_class = SchoolingSerializer
    permission_classes = [permissions.IsAuthenticated]
