from django.contrib.auth.base_user import BaseUserManager

from weducar.apps.administration.models import Employee, Schooling


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, employee=None, **extra_fields):

        if not username:
            raise ValueError("O nome de usuário é obrigatório.")

        if employee is None:
            schooling_id = Schooling.objects.get(
                description='Ensino Superior Completo'
            )

            employee = Employee.objects.get_or_create(
                name=username,
                gender='M',
                birth_date='2000-01-01',
                cpf='00000000000',
                schooling=schooling_id,
            )[0]

        user = self.model(username=username, employee=employee, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, password,  employee=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("O superusuário deve ter is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("O superusuário deve ter is_superuser=True.")

        return self.create_user(username, password, employee=employee, **extra_fields)
