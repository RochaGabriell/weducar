from django.db import models


class History(models.Model):
    history_id = models.AutoField(primary_key=True, db_column='id_historico')
    student_registration = models.ForeignKey(
        'students.Student', models.DO_NOTHING, db_column='aluno_matricula',
    )
    school_id = models.ForeignKey(
        'administration.School', models.DO_NOTHING, db_column='id_escola',
    )
    school_year_id = models.ForeignKey(
        'academics.SchoolYear', models.DO_NOTHING, db_column='id_ano_escolar',
    )
    institution = models.CharField(max_length=45, db_column='estabelecimento')
    year = models.CharField(max_length=45, db_column='ano')
    city_id = models.ForeignKey(
        'locations.City', models.DO_NOTHING, db_column='id_cidade',
    )
    eja = models.IntegerField(blank=True, null=True, db_column='eja')
    resolution = models.CharField(
        max_length=45, blank=True, null=True, db_column='resolucao',
    )
    result = models.CharField(max_length=10, db_column='resultado')
    workload = models.IntegerField(
        blank=True, null=True, db_column='carga_horaria',
    )
    observations = models.TextField(
        blank=True, null=True, db_column='observacoes',
    )

    class Meta:
        db_table = 'historico'
        verbose_name = 'Histórico'
        verbose_name_plural = 'Históricos'
