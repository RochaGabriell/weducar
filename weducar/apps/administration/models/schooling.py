from django.db import models


class Schooling(models.Model):
    schooling_id = models.AutoField(
        primary_key=True, verbose_name='ID da Escolaridade',
        db_column='id_escolaridade'
    )
    description = models.CharField(
        max_length=45, verbose_name='Descrição', db_column='descricao',
    )

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'escolaridade'
        verbose_name = 'Escolaridade'
        verbose_name_plural = 'Escolaridades'
