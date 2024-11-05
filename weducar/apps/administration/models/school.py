from django.db import models


class School(models.Model):
    id = models.AutoField(
        primary_key=True, verbose_name='ID da Escola', db_column='id_escola'
    )
    instance = models.ForeignKey(
        'locations.Instance', models.DO_NOTHING, verbose_name='Instância',
        db_column='id_instancia'
    )
    corporate_name = models.CharField(
        max_length=45, verbose_name='Nome ou Razão Social', db_column='nome_razao'
    )
    trade_name = models.CharField(
        max_length=45, verbose_name='Nome Fantasia', db_column='nome_fantasia'
    )
    address = models.CharField(
        max_length=45, verbose_name='Endereço', db_column='endereco'
    )
    neighborhood = models.CharField(
        max_length=45, verbose_name='Bairro', db_column='bairro'
    )
    email = models.CharField(
        max_length=45, verbose_name='Email'
    )
    postal_code = models.CharField(
        max_length=45, verbose_name='CEP', db_column='cep'
    )
    tax_id = models.CharField(
        max_length=45, verbose_name='CNPJ', db_column='cnpj'
    )
    inep_code = models.CharField(
        max_length=45, verbose_name='Código INEP', db_column='inep'
    )
    logo = models.TextField(
        verbose_name='Logotipo'
    )
    additional_field = models.CharField(
        max_length=45, blank=True, null=True, verbose_name='Campo Adicional',
        db_column='escolascol'
    )

    def __str__(self):
        return f'{self.corporate_name} | {self.instance}'

    class Meta:
        db_table = 'escolas'
        verbose_name = 'Escola'
        verbose_name_plural = 'Escolas'
