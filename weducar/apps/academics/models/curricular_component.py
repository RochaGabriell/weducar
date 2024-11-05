from django.db import models


class CurricularComponent(models.Model):
    id = models.AutoField(
        primary_key=True, db_column='id_componente',
    )
    instance = models.ForeignKey(
        'locations.Instance', models.DO_NOTHING, db_column='id_instancia',
    )
    description = models.CharField(max_length=45, db_column='descricao')

    class Meta:
        db_table = 'componentes_curriculares'
        verbose_name = 'Componente Curricular'
        verbose_name_plural = 'Componentes Curriculares'
