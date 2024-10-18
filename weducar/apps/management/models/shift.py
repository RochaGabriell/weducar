from django.db import models


class Shift(models.Model):
    shift_id = models.AutoField(primary_key=True, db_column='id_turno')
    instance_id = models.ForeignKey(
        'locations.Instance', models.DO_NOTHING, db_column='id_instancia'
    )
    description = models.CharField(max_length=45, db_column='descricao')

    class Meta:
        db_table = 'turnos'
        verbose_name = 'Turno'
        verbose_name_plural = 'Turnos'
