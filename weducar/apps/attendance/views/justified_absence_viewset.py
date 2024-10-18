from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions

from ..serializers.justified_absence_serializer import JustifiedAbsenceSerializer
from ..models import JustifiedAbsence


class JustifiedAbsenceViewSet(viewsets.ModelViewSet):
    queryset = JustifiedAbsence.objects.all()
    serializer_class = JustifiedAbsenceSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
