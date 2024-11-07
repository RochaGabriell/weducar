from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions

from ..serializers.instance_serializer import InstanceSerializer
from ..models import Instance


class InstanceViewSet(viewsets.ModelViewSet):
    queryset = Instance.objects.all()
    serializer_class = InstanceSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    
    # def get_queryset(self):
    #     queryset = super().get_queryset()
        
    #     return queryset
