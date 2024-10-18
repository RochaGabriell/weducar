from django.db import models


class Instance(models.Model):
    instance_id = models.AutoField(primary_key=True, db_column='id_instancia')
    state_id = models.ForeignKey(
        'locations.State', models.DO_NOTHING, db_column='id_estado',
    )
    name = models.CharField(max_length=45, db_column='nome')
    address = models.CharField(max_length=45, db_column='endereco')
    neighborhood = models.CharField(max_length=45, db_column='bairro')
    postal_code = models.CharField(max_length=45, db_column='cep')
    tax_id = models.CharField(max_length=45, db_column='cnpj')

    class Meta:
        db_table = 'instancias'
        verbose_name = 'Instância'
        verbose_name_plural = 'Instâncias'
