from django.db import models


class Week(models.Model):
    day_id = models.AutoField(primary_key=True, db_column='id_dia')
    description = models.CharField(max_length=45, db_column='descricao')

    class Meta:
        db_table = 'semana'
        verbose_name = 'Dia da Semana'
        verbose_name_plural = 'Dias da Semana'
