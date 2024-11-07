from rest_framework import viewsets, permissions

from ..serializers.student_status_serializer import StudentStatusSerializer
from ..models import StudentStatus


class StudentStatusViewSet(viewsets.ModelViewSet):
    queryset = StudentStatus.objects.all()
    serializer_class = StudentStatusSerializer
    permission_classes = [permissions.IsAuthenticated]
