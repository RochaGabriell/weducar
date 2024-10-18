from django.db import models


class CurricularMatrix(models.Model):
    matrix_id = models.AutoField(primary_key=True, db_column='id_matriz')
    description = models.CharField(max_length=45, db_column='descricao')
    matrix_year = models.IntegerField(db_column='ano_matriz')

    class Meta:
        db_table = 'matriz_curricular'
        verbose_name = 'Matriz Curricular'
        verbose_name_plural = 'Matrizes Curriculares'
