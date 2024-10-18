from rest_framework_simplejwt.views import TokenObtainPairView

from ..serializers.my_token_obtain_pair_serializer import MyTokenObtainPairSerializer


class MyTokenObtainPairViewSet(TokenObtainPairView):

    serializer_class = MyTokenObtainPairSerializer
