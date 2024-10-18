from django.db import models


class AcademicYear(models.Model):
    academic_year_id = models.AutoField(
        primary_key=True, db_column='id_ano_letivo',
    )
    description = models.IntegerField(db_column='descricao')

    class Meta:
        db_table = 'anos_letivos'
        verbose_name = 'Ano Letivo'
        verbose_name_plural = 'Anos Letivos'
