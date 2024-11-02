from django.db import models


class Room(models.Model):
    classroom_id = models.AutoField(
        primary_key=True, verbose_name='ID da Sala', db_column='id_sala'
    )
    school = models.ForeignKey(
        'administration.School', models.DO_NOTHING, verbose_name='Escola',
        db_column='id_escola'
    )
    description = models.CharField(
        max_length=45, verbose_name='Descrição', db_column='descricao'
    )
    
    def __str__(self):
        return f'{self.description} - {self.school.corporate_name}'

    class Meta:
        db_table = 'salas'
        verbose_name = 'Sala'
        verbose_name_plural = 'Salas'
