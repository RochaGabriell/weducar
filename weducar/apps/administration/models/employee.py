from django.db import models


class Employee(models.Model):
    employee_id = models.AutoField(
        primary_key=True, db_column='id_funcionario',
    )
    schooling = models.ForeignKey(
        'administration.Schooling', models.DO_NOTHING, db_column='id_escolaridade',
    )
    name = models.CharField(max_length=255, db_column='nome')
    gender = models.CharField(max_length=1, db_column='sexo')
    birth_date = models.DateField(db_column='data_nascimento')
    rg = models.CharField(
        max_length=45, blank=True, null=True, db_column='rg',
    )
    cpf = models.CharField(max_length=11, db_column='cpf', unique=True)
    photo = models.TextField(blank=True, null=True, db_column='foto')

    class Meta:
        db_table = 'funcionarios'
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
