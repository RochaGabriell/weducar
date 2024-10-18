from django.db import models


class CurricularComponentMatrix(models.Model):
    matrix_component_id = models.AutoField(
        primary_key=True, db_column='id_matriz_componente',
    )
    component_id = models.ForeignKey(
        'academics.CurricularComponent', models.DO_NOTHING, db_column='id_componente'
    )
    matrix_id = models.ForeignKey(
        'academics.CurricularMatrix', models.DO_NOTHING, db_column='id_matriz'
    )
    stage = models.CharField(max_length=2)
    workload = models.IntegerField()

    class Meta:
        db_table = 'matriz_componentes'
        verbose_name = 'Componente da Matriz Curricular'
        verbose_name_plural = 'Componentes da Matriz Curricular'
