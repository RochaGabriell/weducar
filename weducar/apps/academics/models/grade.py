from django.db import models


class Grade(models.Model):
    grade_id = models.AutoField(primary_key=True, db_column='id_nota')
    diary_id = models.ForeignKey(
        'academics.Diary', models.DO_NOTHING, db_column='id_diario'
    )
    evaluation_id = models.ForeignKey(
        'academics.Evaluation', models.DO_NOTHING, db_column='id_avaliacao'
    )
    student_registration = models.ForeignKey(
        'students.Student', models.DO_NOTHING, db_column='aluno_matricula'
    )
    grade = models.DecimalField(max_digits=2, decimal_places=2)

    class Meta:
        db_table = 'notas'
        verbose_name = 'Nota'
        verbose_name_plural = 'Notas'
