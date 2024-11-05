from django.db import models


class StudentStatus(models.Model):
    id = models.AutoField(
        primary_key=True, verbose_name='ID da Situação Aluno', db_column='id_situacao_aluno',
    )
    description = models.CharField(
        max_length=45, verbose_name='Descrição', db_column='descricao',
    )

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'situacao_aluno'
        verbose_name = 'Situação do Aluno'
        verbose_name_plural = 'Situações do Aluno'
