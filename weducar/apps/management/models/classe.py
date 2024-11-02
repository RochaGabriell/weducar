from django.db import models


class Classe(models.Model):
    class_id = models.AutoField(
        primary_key=True, verbose_name='ID da Turma', db_column='id_turma'
    )
    shift_id = models.ForeignKey(
        'management.Shift', models.DO_NOTHING, verbose_name='Turno', db_column='id_turno'
    )
    school_year_id = models.ForeignKey(
        'academics.SchoolYear', models.DO_NOTHING, verbose_name='Ano Escolar', db_column='id_ano_escolar'
    )
    room_id = models.ForeignKey(
        'administration.Room', models.DO_NOTHING, verbose_name='Sala', db_column='id_sala'
    )
    description = models.CharField(
        max_length=45, verbose_name='Descrição', db_column='descricao'
    )
    start_time = models.CharField(
        max_length=45, verbose_name='Horário de Início', db_column='horario_inicio'
    )
    end_time = models.CharField(
        max_length=45, verbose_name='Horário de Fim', db_column='horario_fim'
    )
    eja = models.IntegerField(
        verbose_name='EJA', db_column='eja'
    )
    
    def __str__(self):
        return self.description

    class Meta:
        db_table = 'turmas'
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'
