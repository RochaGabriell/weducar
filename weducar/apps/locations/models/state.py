from django.db import models


class State(models.Model):
    state_id = models.AutoField(
        primary_key=True, verbose_name='ID do Estado', db_column='id_estado',
    )
    uf = models.CharField(
        max_length=2, verbose_name='UF', db_column='uf',
    )
    name = models.CharField(
        max_length=45, verbose_name='Nome', db_column='nome',
    )
    
    def __str__(self):
        return f'{self.name} - {self.uf}'

    class Meta:
        db_table = 'estados'
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
