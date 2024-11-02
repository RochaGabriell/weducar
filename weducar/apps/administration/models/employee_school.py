from django.db import models

USER_TYPE = (
    ('super_admin', 'Super Admin'),
    ('admin', 'Admin'),
    ('gestor', 'Gestor'),
    ('docente', 'Docente'),
)


class EmployeeSchool(models.Model):
    employee_id = models.ForeignKey(
        'administration.Employee', models.DO_NOTHING, verbose_name='Funcionário', db_column='id_funcionario',
    )
    school_id = models.ForeignKey(
        'administration.School', models.DO_NOTHING, verbose_name='Escola',
        db_column='id_escola',
    )
    contract_type_id = models.ForeignKey(
        'administration.ContractType', models.DO_NOTHING, verbose_name='Tipo de Contrato',
        db_column='id_contrato',
    )
    academic_year_id = models.ForeignKey(
        'academics.AcademicYear', models.DO_NOTHING, verbose_name='Ano Letivo',
        db_column='id_ano_letivo',
    )
    position_id = models.ForeignKey(
        'administration.Position', models.DO_NOTHING, verbose_name='Cargo',
        db_column='id_cargo',
    )
    user_type = models.CharField(
        max_length=11, choices=USER_TYPE, verbose_name='Tipo de Usuário',
        db_column='tipo',
    )

    def __str__(self):
        return f'{self.employee_id.name} - {self.school_id.corporate_name} - {self.school_id.instance_id.name}'

    class Meta:
        db_table = 'funcionarios_escolas'
        unique_together = (('employee_id', 'school_id'),)
        verbose_name = 'Funcionário alocado na escola'
        verbose_name_plural = 'Funcionários alocados nas escolas'
