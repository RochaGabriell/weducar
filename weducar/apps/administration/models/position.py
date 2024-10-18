from django.db import models


class Position(models.Model):
    position_id = models.AutoField(primary_key=True, db_column='id_cargo')
    description = models.CharField(max_length=45, db_column='descricao')

    class Meta:
        db_table = 'cargos'
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
