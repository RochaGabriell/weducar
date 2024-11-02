from django.db import models


class Shift(models.Model):
    shift_id = models.AutoField(
        primary_key=True, verbose_name='ID do Turno', db_column='id_turno'
    )
    instance_id = models.ForeignKey(
        'locations.Instance', models.DO_NOTHING, verbose_name='Instância', db_column='id_instancia'
    )
    description = models.CharField(
        max_length=45, verbose_name='Descrição', db_column='descricao'
    )

    def __str__(self):
        return f'{self.description} - {self.instance_id.name}'

    class Meta:
        db_table = 'turnos'
        verbose_name = 'Turno'
        verbose_name_plural = 'Turnos'
