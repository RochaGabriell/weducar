from django.db import models


class StudentClasses(models.Model):
    class_id_student = models.AutoField(
        primary_key=True, verbose_name='ID da Turma do Aluno', db_column='id_turma_aluno',
    )
    class_id = models.ForeignKey(
        'management.Classe', models.DO_NOTHING, verbose_name='Turma', db_column='id_turma'
    )
    student_enrollment = models.ForeignKey(
        'students.Student', models.DO_NOTHING, verbose_name='Matrícula do Aluno', db_column='aluno_matricula'
    )

    def to_dict(self):
        return {
            # 'class_id_student': self.class_id_student,
            'id': self.class_id.class_id,
            'description': str(self.class_id),
            'school_year': {
                'id': self.class_id.school_year_id.school_year_id,
                'description': self.class_id.school_year_id.series,
            }

        }

    def __str__(self):
        return f'{self.student_enrollment} - {self.class_id}'

    class Meta:
        db_table = 'turmas_aluno'
        verbose_name = 'Turma do Aluno'
        verbose_name_plural = 'Turmas dos Alunos'
