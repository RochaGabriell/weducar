from django.db import models


class City(models.Model):
    id = models.AutoField(
        primary_key=True, verbose_name='ID da Cidade', db_column='id_cidade',
    )
    state = models.ForeignKey(
        'locations.State', models.DO_NOTHING, verbose_name='Estado',
        db_column='id_estado'
    )
    name = models.CharField(
        max_length=45, verbose_name='Nome', db_column='nome',
    )

    def __str__(self):
        return f'{self.name} - {self.state.uf}'

    class Meta:
        db_table = 'cidades'
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'
