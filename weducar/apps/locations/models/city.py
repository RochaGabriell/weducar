from django.db import models


class City(models.Model):
    city_id = models.AutoField(primary_key=True, db_column='id_cidade')
    state_id = models.ForeignKey(
        'locations.State', models.DO_NOTHING, db_column='id_estado'
    )
    name = models.CharField(max_length=45, db_column='nome')

    class Meta:
        db_table = 'cidades'
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'
