from django.db import models


class ScheduleGrid(models.Model):
    schedule_grid_id = models.AutoField(
        primary_key=True, db_column='id_grade_horario',
    )
    diary = models.ForeignKey(
        'academics.Diary', models.DO_NOTHING, db_column='id_diario',
    )
    day = models.ForeignKey(
        'management.Week', models.DO_NOTHING, db_column='id_dia',
    )
    class_time = models.ForeignKey(
        'administration.ClassSchedule', models.DO_NOTHING, db_column='id_horario_aula',
    )

    class Meta:
        db_table = 'grades_horarios'
        verbose_name = 'Grade de horário'
        verbose_name_plural = 'Grades de horários'
