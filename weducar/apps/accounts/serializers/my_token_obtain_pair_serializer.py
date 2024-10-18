from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.conf import settings
import jwt

from weducar.apps.administration.serializers import EmployeeSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)

        user = self.user

        decoded_token = jwt.decode(
            data.get('access'),
            settings.SECRET_KEY,
            algorithms=[settings.SIMPLE_JWT.get('ALGORITHM')]
        )

        user_info = {
            'username': user.username,
            'user_type': user.user_type,
            'access_count': user.access_count,
            'last_access': user.last_access,
            'is_active': user.is_active,
            'is_staff': user.is_staff,
            'is_superuser': user.is_superuser,
            'employee': EmployeeSerializer(user.employee).data
        }

        data.update({
            'expires_in': decoded_token.get('exp') - int(decoded_token.get('iat')),
            'token_type': 'Bearer',
            'info': user_info,
        })

        return data
