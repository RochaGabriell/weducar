from django.db import models


class ClassSchedule(models.Model):
    class_schedule_id = models.AutoField(
        primary_key=True, db_column='id_horario_aula',
    )
    shift = models.ForeignKey(
        'management.Shift', models.DO_NOTHING, db_column='id_turno',
    )
    description = models.CharField(max_length=45)
    schedule_time = models.CharField(max_length=45)
    last_updated = models.DateField(db_column='data_atualizacao')

    class Meta:
        db_table = 'horarios_aulas'
        verbose_name = 'Horário de aula'
        verbose_name_plural = 'Horários de aulas'
