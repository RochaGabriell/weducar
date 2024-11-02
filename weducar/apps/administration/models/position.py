from django.db import models


class Position(models.Model):
    position_id = models.AutoField(
        primary_key=True, verbose_name='ID do Cargo', db_column='id_cargo',
    )
    description = models.CharField(
        max_length=45, verbose_name='Descrição', db_column='descricao',
    )

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'cargos'
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
