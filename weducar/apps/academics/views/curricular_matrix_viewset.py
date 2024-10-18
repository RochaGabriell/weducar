from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions

from ..serializers.curricular_matrix_serializer import CurricularMatrixSerializer
from ..models import CurricularMatrix


class CurricularMatrixViewSet(viewsets.ModelViewSet):
    queryset = CurricularMatrix.objects.all()
    serializer_class = CurricularMatrixSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
