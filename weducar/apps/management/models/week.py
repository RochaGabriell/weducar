from django.db import models


class Week(models.Model):
    day_id = models.AutoField(
        primary_key=True, verbose_name='ID do Dia', db_column='id_dia'
    )
    description = models.CharField(
        max_length=45, verbose_name='Descrição', db_column='descricao'
    )

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'semana'
        verbose_name = 'Dia da Semana'
        verbose_name_plural = 'Dias da Semana'
