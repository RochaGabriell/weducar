from django.db import models


class JustifiedAbsence(models.Model):
    justified_absence_id = models.AutoField(
        primary_key=True, db_column='id_falta_justificada',
    )
    student_class_id = models.ForeignKey(
        'students.StudentClasses', models.DO_NOTHING, db_column='id_turma_aluno',
    )
    start_date = models.DateField(db_column='data_inicio')
    end_date = models.DateField(blank=True, null=True, db_column='data_fim')
    justification = models.TextField(db_column='justificativa')
    file = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'faltas_justificadas'
        verbose_name = 'Falta Justificada'
        verbose_name_plural = 'Faltas Justificadas'
