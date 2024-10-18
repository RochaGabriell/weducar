from django.db import models


class SysPresence(models.Model):
    date = models.DateField(db_column='data')
    status = models.IntegerField(db_column='situacao')
    student_class_id = models.ForeignKey(
        'students.StudentClasses', models.DO_NOTHING, db_column='id_turma_aluno'
    )

    class Meta:
        db_table = 'sys_presenca'
        verbose_name = 'Presença'
        verbose_name_plural = 'Presenças'
