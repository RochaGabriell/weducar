from django.db import models


class History(models.Model):
    history_id = models.AutoField(
        primary_key=True, verbose_name='ID do Histórico', db_column='id_historico'
    )
    student_registration = models.ForeignKey(
        'students.Student', models.DO_NOTHING, verbose_name='Matrícula do Aluno', db_column='aluno_matricula'
    )
    school_id = models.ForeignKey(
        'administration.School', models.DO_NOTHING, verbose_name='Escola', db_column='id_escola'
    )
    school_year_id = models.ForeignKey(
        'academics.SchoolYear', models.DO_NOTHING, verbose_name='Ano Escolar', db_column='id_ano_escolar'
    )
    institution = models.CharField(
        max_length=45, verbose_name='Estabelecimento', db_column='estabelecimento'
    )
    year = models.CharField(
        max_length=45, verbose_name='Ano', db_column='ano'
    )
    city_id = models.ForeignKey(
        'locations.City', models.DO_NOTHING, verbose_name='Cidade', db_column='id_cidade'
    )
    eja = models.IntegerField(
        blank=True, null=True, verbose_name='EJA', db_column='eja'
    )
    resolution = models.CharField(
        max_length=45, blank=True, null=True, verbose_name='Resolução', db_column='resolucao'
    )
    result = models.CharField(
        max_length=10, verbose_name='Resultado', db_column='resultado'
    )
    workload = models.IntegerField(
        blank=True, null=True, verbose_name='Carga Horária', db_column='carga_horaria'
    )
    observations = models.TextField(
        blank=True, null=True, verbose_name='Observações', db_column='observacoes'
    )

    class Meta:
        db_table = 'historico'
        verbose_name = 'Histórico'
        verbose_name_plural = 'Históricos'
