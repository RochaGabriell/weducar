from django.db import models


class Instance(models.Model):
    instance_id = models.AutoField(
        primary_key=True, verbose_name='ID da Instância', db_column='id_instancia'
    )
    state_id = models.ForeignKey(
        'locations.State', models.DO_NOTHING, verbose_name='Estado', db_column='id_estado'
    )
    name = models.CharField(
        max_length=45, verbose_name='Nome', db_column='nome'
    )
    address = models.CharField(
        max_length=45, verbose_name='Endereço', db_column='endereco'
    )
    neighborhood = models.CharField(
        max_length=45, verbose_name='Bairro', db_column='bairro'
    )
    postal_code = models.CharField(
        max_length=45, verbose_name='CEP', db_column='cep'
    )
    tax_id = models.CharField(
        max_length=45, verbose_name='CNPJ', db_column='cnpj'
    )
    
    def __str__(self):
        return f'{self.name} - {self.state_id}'

    class Meta:
        db_table = 'instancias'
        verbose_name = 'Instância'
        verbose_name_plural = 'Instâncias'
