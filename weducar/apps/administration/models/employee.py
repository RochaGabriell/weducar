from django.db import models

GENDER_CHOICES = [
    ('M', 'Masculino'),
    ('F', 'Feminino'),
]


class Employee(models.Model):
    employee_id = models.AutoField(
        primary_key=True, verbose_name='ID do Funcionário', db_column='id_funcionario'
    )
    schooling = models.ForeignKey(
        'administration.Schooling', models.DO_NOTHING, verbose_name='Escolaridade', db_column='id_escolaridade'
    )
    name = models.CharField(
        max_length=255, verbose_name='Nome', db_column='nome',
    )
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, verbose_name='Sexo', db_column='sexo',
    )
    birth_date = models.DateField(
        verbose_name='Data de Nascimento', db_column='data_nascimento',
    )
    rg = models.CharField(
        max_length=45, blank=True, null=True, verbose_name='RG', db_column='rg'
    )
    cpf = models.CharField(
        max_length=11, verbose_name='CPF', db_column='cpf', unique=True,
    )
    photo = models.TextField(
        blank=True, null=True, verbose_name='Foto', db_column='foto',
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'funcionarios'
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
