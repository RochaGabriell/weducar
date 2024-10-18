from django.db import models


class Housing(models.Model):
    housing_id = models.AutoField(primary_key=True, db_column='id_moradia')
    description = models.CharField(max_length=255, db_column='descricao')

    class Meta:
        db_table = 'moradia'
        verbose_name = 'Moradia'
        verbose_name_plural = 'Moradias'
