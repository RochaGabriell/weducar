from django.db import models


class HistoryArea(models.Model):
    school_area_id = models.AutoField(
        primary_key=True, verbose_name='ID da Área Escolar', db_column='id_escolar_area',
    )
    history_id = models.ForeignKey(
        'students.History', models.DO_NOTHING, verbose_name='Histórico', db_column='id_historico'
    )
    component_id = models.ForeignKey(
        'academics.CurricularComponent', models.DO_NOTHING, verbose_name='Componente Curricular', db_column='id_componente'
    )
    grade = models.DecimalField(
        max_digits=2, decimal_places=2, verbose_name='Nota', db_column='nota'
    )
    workload = models.IntegerField(
        blank=True, null=True, verbose_name='Carga Horária', db_column='carga_horaria'
    )

    class Meta:
        db_table = 'historico_areas'
        verbose_name = 'Área do Histórico'
        verbose_name_plural = 'Áreas do Histórico'
