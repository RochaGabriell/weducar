from django.db import models


class Schooling(models.Model):
    Schooling_id = models.AutoField(
        primary_key=True, db_column='id_escolaridade',
    )
    description = models.CharField(max_length=45, db_column='descricao')

    class Meta:
        db_table = 'escolaridade'
        verbose_name = 'Escolaridade'
        verbose_name_plural = 'Escolaridades'
