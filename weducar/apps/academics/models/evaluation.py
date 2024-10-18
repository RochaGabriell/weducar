from django.db import models


class Evaluation(models.Model):
    evaluation_id = models.AutoField(
        primary_key=True, db_column='id_avaliacao',
    )
    instance_id = models.ForeignKey(
        'locations.Instance', models.DO_NOTHING, db_column='id_instancia',
    )
    academic_year_id = models.ForeignKey(
        'academics.AcademicYear', models.DO_NOTHING, db_column='id_ano_letivo',
    )
    description = models.CharField(max_length=45, db_column='descricao')
    recovery = models.IntegerField(db_column='recuperacao')
    group = models.CharField(
        max_length=45, blank=True, null=True, db_column='grupo',
    )

    class Meta:
        db_table = 'avaliacoes'
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
