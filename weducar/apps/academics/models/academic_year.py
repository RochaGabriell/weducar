from django.db import models


class AcademicYear(models.Model):
    academic_year_id = models.AutoField(
        primary_key=True, verbose_name='ID do Ano Letivo', db_column='id_ano_letivo',
    )
    description = models.CharField(
        max_length=10, verbose_name='Descrição', db_column='descricao',
    )

    def __str__(self):
        return str(self.description)

    class Meta:
        db_table = 'anos_letivos'
        verbose_name = 'Ano Letivo'
        verbose_name_plural = 'Anos Letivos'
