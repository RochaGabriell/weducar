from django.db import models


class Classe(models.Model):
    class_id = models.AutoField(primary_key=True, db_column='id_turma')
    shift_id = models.ForeignKey(
        'management.Shift', models.DO_NOTHING, db_column='id_turno'
    )
    school_year_id = models.ForeignKey(
        'academics.SchoolYear', models.DO_NOTHING, db_column='id_ano_escolar'
    )
    room_id = models.ForeignKey(
        'administration.Room', models.DO_NOTHING, db_column='id_sala'
    )
    description = models.CharField(max_length=45, db_column='descricao')
    start_time = models.CharField(max_length=45, db_column='horario_inicio')
    end_time = models.CharField(max_length=45, db_column='horario_fim')
    eja = models.IntegerField(db_column='eja')

    class Meta:
        db_table = 'turmas'
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'
