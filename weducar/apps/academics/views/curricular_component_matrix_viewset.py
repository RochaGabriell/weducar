from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions

from ..serializers.curricular_component_matrix_serializer import CurricularComponentMatrixSerializer
from ..models import CurricularComponentMatrix


class CurricularComponentMatrixViewSet(viewsets.ModelViewSet):
    queryset = CurricularComponentMatrix.objects.all()
    serializer_class = CurricularComponentMatrixSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
