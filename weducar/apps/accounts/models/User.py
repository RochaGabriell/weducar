from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from weducar.apps.accounts.managers import CustomUserManager
from weducar.apps.locations.models import Instance
from weducar.apps.administration.models import EmployeeSchool


class User(AbstractBaseUser, PermissionsMixin):
    employee = models.ForeignKey(
        'administration.Employee', models.DO_NOTHING, verbose_name='Funcionário', db_column='id_funcionario'
    )
    username = models.CharField(
        max_length=45, unique=True, verbose_name='Nome de Usuário', db_column='usuario'
    )
    # password = models.CharField(max_length=45, db_column='senha')
    # status = models.BooleanField(default=True, db_column='status')
    access_count = models.IntegerField(
        default=0, verbose_name='Número de Acessos', db_column='acessos'
    )
    last_access = models.DateTimeField(
        blank=True, null=True, verbose_name='Último Acesso', db_column='ultimo_acesso'
    )

    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    is_staff = models.BooleanField(
        default=False, verbose_name='Membro da Equipe',
    )
    is_superuser = models.BooleanField(
        default=False, verbose_name='Superusuário',
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def get_instances(self):
        if not self.is_superuser:
            employee_schools = EmployeeSchool.objects.filter(
                employee_id=self.employee
                # realizar um join e carregar os dados de school_id e seu respectivo instance_id
            ).select_related('school_id__instance')

            unique_instances = {}

            for emp_school in employee_schools:
                instance_id = emp_school.school_id.instance
                if instance_id not in unique_instances:
                    unique_instances[instance_id] = {
                        'id': emp_school.school_id.instance_id.instance_id,
                        'name': emp_school.school_id.instance_id.name,
                        'user_type': emp_school.user_type,
                    }

            return list(unique_instances.values())
        else:
            instances = Instance.objects.all()
            instances_list = [instance.to_dict() for instance in instances]
            return instances_list

    def get_schools(self):
        employee_schools = EmployeeSchool.objects.filter(
            employee_id=self.employee
        ).select_related('school_id__instance')

        instances_data = [
            {
                'id': emp_school.school_id.school_id,
                'name': emp_school.school_id.corporate_name,
                'instance': emp_school.school_id.instance_id.name,
                'user_type': emp_school.user_type,
            }
            for emp_school in employee_schools
        ]

        return instances_data

    def __str__(self):
        return f'{self.username} - {self.employee.name}'

    class Meta:
        db_table = 'usuarios'
        unique_together = (('id', 'employee'),)
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
