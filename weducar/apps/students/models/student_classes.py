from django.db import models


class StudentClasses(models.Model):
    class_id_student = models.AutoField(
        primary_key=True, db_column='id_turma_aluno',
    )
    class_id = models.ForeignKey(
        'management.Classe', models.DO_NOTHING, db_column='id_turma'
    )
    student_enrollment = models.ForeignKey(
        'students.Student', models.DO_NOTHING, db_column='aluno_matricula'
    )

    class Meta:
        db_table = 'turmas_aluno'
        verbose_name = 'Turma do Aluno'
        verbose_name_plural = 'Turmas dos Alunos'
