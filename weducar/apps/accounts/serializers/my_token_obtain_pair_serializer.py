from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.utils import timezone
from django.conf import settings
import jwt

from weducar.apps.administration.serializers import EmployeeSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)

        user = self.user

        user.access_count += 1
        user.last_access = timezone.now()
        user.save(update_fields=['access_count', 'last_access'])

        decoded_token = jwt.decode(
            data.get('access'),
            settings.SECRET_KEY,
            algorithms=[settings.SIMPLE_JWT.get('ALGORITHM')]
        )

        # Serializa employee sem o campo 'schooling'
        employee_data = EmployeeSerializer(user.employee).data
        employee_data.pop('schooling', None)

        user_info = {
            'id': user.id,
            'username': user.username,
            'access_count': user.access_count,
            'last_access': user.last_access,
            'is_active': user.is_active,
            'is_staff': user.is_staff,
            'is_superuser': user.is_superuser,
            'employee': employee_data,
            'instances': user.get_instances(),
        }

        data.update({
            'expires_in': decoded_token.get('exp') - int(decoded_token.get('iat')),
            'token_type': 'Bearer',
            'user_info': user_info,
        })

        return data
