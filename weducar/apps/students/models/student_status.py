from django.db import models


class StudentStatus(models.Model):
    student_status_id = models.AutoField(
        primary_key=True, db_column='id_situacao_aluno',
    )
    description = models.CharField(max_length=45, db_column='descricao')

    class Meta:
        db_table = 'situacao_aluno'
        verbose_name = 'Situação do Aluno'
        verbose_name_plural = 'Situações do Aluno'
