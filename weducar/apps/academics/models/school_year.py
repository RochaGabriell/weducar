from django.db import models


class SchoolYear(models.Model):
    school_year_id = models.AutoField(
        primary_key=True, db_column='id_ano_escolar',
    )
    academic_year_id = models.ForeignKey(
        'academics.AcademicYear', models.DO_NOTHING, db_column='id_ano_letivo',
    )
    school_id = models.ForeignKey(
        'administration.School', models.DO_NOTHING, db_column='id_escola',
    )
    series = models.CharField(max_length=45, db_column='serie')
    stage = models.CharField(max_length=2, db_column='etapa')
    curriculum_matrix_id = models.ForeignKey(
        'academics.CurricularMatrix', models.DO_NOTHING, db_column='id_matriz',
    )

    class Meta:
        db_table = 'anos_escolares'
        verbose_name = 'Ano Escolar'
        verbose_name_plural = 'Anos Escolares'
