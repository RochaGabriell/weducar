from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from weducar.apps.accounts.managers import CustomUserManager


USER_TYPE = (
    ('super_admin', 'Super Admin'),
    ('admin', 'Admin'),
    ('gestor', 'Gestor'),
    ('docente', 'Docente'),
)


class User(AbstractBaseUser, PermissionsMixin):
    employee = models.ForeignKey(
        'administration.Employee', models.DO_NOTHING, db_column='id_funcionario',
    )
    user_type = models.CharField(
        max_length=11, choices=USER_TYPE, db_column='tipo',
    )
    username = models.CharField(
        max_length=45, unique=True, db_column='usuario',
    )
    # password = models.CharField(max_length=45, db_column='senha')
    # status = models.BooleanField(default=True, db_column='status')
    access_count = models.IntegerField(default=0, db_column='acessos')
    last_access = models.DateTimeField(
        blank=True, null=True, db_column='ultimo_acesso',
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        db_table = 'usuarios'
        unique_together = (('id', 'employee'),)
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
