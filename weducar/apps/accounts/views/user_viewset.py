from rest_framework import viewsets, permissions, response
from rest_framework.decorators import api_view, permission_classes

from ..serializers.user_serializer import UserSerializer, UserCreateSerializer
from ..models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        return UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]


@ api_view(['GET'])
@ permission_classes([permissions.IsAuthenticated])
def get_profile(request):
    """
    Endpoint da API que permite que o perfil do usuário seja visualizado. (GET)
    """
    user = request.user
    serializer = UserSerializer(user)
    return response.Response(serializer.data)
