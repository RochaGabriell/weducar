from django.db import models


class Room(models.Model):
    classroom_id = models.AutoField(primary_key=True, db_column='id_sala')
    school = models.ForeignKey(
        'administration.School', models.DO_NOTHING, db_column='id_escola',
    )
    description = models.CharField(max_length=45, db_column='descricao')

    class Meta:
        db_table = 'salas'
        verbose_name = 'Sala'
        verbose_name_plural = 'Salas'
