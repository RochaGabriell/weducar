from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions

from ..serializers.curricular_component_serializer import CurricularComponentSerializer
from ..models import CurricularComponent


class CurricularComponentViewSet(viewsets.ModelViewSet):
    queryset = CurricularComponent.objects.all()
    serializer_class = CurricularComponentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]