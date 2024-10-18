from django.db import models


class State(models.Model):
    state_id = models.AutoField(primary_key=True, db_column='id_estado')
    uf = models.CharField(max_length=2, db_column='uf')
    name = models.CharField(max_length=45, db_column='nome')

    class Meta:
        db_table = 'estados'
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
