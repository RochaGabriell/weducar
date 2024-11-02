from django.db import models

STAGE = (
    ('EI', 'Educação Infantil'),
    ('EF', 'Ensino Fundamental')
)


class SchoolYear(models.Model):
    school_year_id = models.AutoField(
        primary_key=True, verbose_name='ID do Ano Escolar', db_column='id_ano_escolar',
    )
    academic_year_id = models.ForeignKey(
        'academics.AcademicYear', models.DO_NOTHING, verbose_name='Ano Letivo',
        db_column='id_ano_letivo',
    )
    school_id = models.ForeignKey(
        'administration.School', models.DO_NOTHING, verbose_name='Escola',
        db_column='id_escola',
    )
    series = models.CharField(
        max_length=45, verbose_name='Série', db_column='serie',
    )
    stage = models.CharField(
        max_length=2, choices=STAGE, verbose_name='Etapa', db_column='etapa',
    )
    curriculum_matrix_id = models.ForeignKey(
        'academics.CurricularMatrix', models.DO_NOTHING, verbose_name='Matriz Curricular',
        db_column='id_matriz',
    )

    def __str__(self):
        return f'{self.series} - {self.stage} - {self.academic_year_id.description}'

    class Meta:
        db_table = 'anos_escolares'
        verbose_name = 'Ano Escolar'
        verbose_name_plural = 'Anos Escolares'
