from django.db import models


class LessonContent(models.Model):
    lesson_content_id = models.AutoField(
        primary_key=True, db_column='id_conteudo_aula',
    )
    diary_id = models.ForeignKey(
        'academics.Diary', models.DO_NOTHING, db_column='id_diario',
    )
    schedule_id = models.ForeignKey(
        'administration.ScheduleGrid', models.DO_NOTHING, db_column='id_grade_horario',
    )
    description = models.TextField(db_column='descricao')
    status = models.CharField(
        max_length=1, blank=True, null=True, db_column='status',
    )
    registration_date = models.DateField(db_column='data_registro')

    class Meta:
        db_table = 'conteudo_aula'
        verbose_name = 'Conteúdo da Aula'
        verbose_name_plural = 'Conteúdos das Aulas'
