from django.db import models


class EmployeeSchool(models.Model):
    employee_id = models.ForeignKey(
        'administration.Employee', models.DO_NOTHING, db_column='id_funcionario'
    )
    school_id = models.ForeignKey(
        'administration.School', models.DO_NOTHING, db_column='id_escola'
    )
    contract_type_id = models.ForeignKey(
        'administration.ContractType', models.DO_NOTHING, db_column='id_contrato'
    )
    academic_year_id = models.ForeignKey(
        'academics.AcademicYear', models.DO_NOTHING, db_column='id_ano_letivo'
    )
    position_id = models.ForeignKey(
        'administration.Position', models.DO_NOTHING, db_column='id_cargo'
    )

    class Meta:
        db_table = 'funcionarios_escolas'
        unique_together = (('employee_id', 'school_id'),)
        verbose_name = 'Funcionário alocado na escola'
        verbose_name_plural = 'Funcionários alocados nas escolas'
