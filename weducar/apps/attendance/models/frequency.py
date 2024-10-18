from django.db import models


class Frequency(models.Model):
    frequency_id = models.AutoField(
        primary_key=True, db_column='id_frequencia',
    )
    lesson_content_id = models.ForeignKey(
        'academics.LessonContent', models.DO_NOTHING, db_column='id_conteudo_aula'
    )
    student_enrollment = models.ForeignKey(
        'students.Student', models.DO_NOTHING, db_column='aluno_matricula'
    )
    presence = models.CharField(max_length=1)

    class Meta:
        db_table = 'frequencias'
        verbose_name = 'Frequência'
        verbose_name_plural = 'Frequências'
