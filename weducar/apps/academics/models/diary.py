from django.db import models


class Diary(models.Model):
    diary_id = models.AutoField(primary_key=True, db_column='id_diario')
    employee_id = models.ForeignKey(
        'administration.Employee', models.DO_NOTHING, db_column='id_funcionario'
    )
    matrix_component_id = models.ForeignKey(
        'academics.CurricularComponentMatrix', models.DO_NOTHING,
        db_column='id_matriz_componente'
    )
    class_id = models.ForeignKey(
        'management.Classe', models.DO_NOTHING, db_column='id_turma'
    )

    class Meta:
        db_table = 'diarios'
        verbose_name = 'Diário'
        verbose_name_plural = 'Diários'
