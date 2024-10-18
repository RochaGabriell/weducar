from django.db import models


class School(models.Model):
    school_id = models.AutoField(primary_key=True, db_column='id_escola')
    instance_id = models.ForeignKey(
        'locations.Instance', models.DO_NOTHING, db_column='id_instancia',
    )
    corporate_name = models.CharField(max_length=45, db_column='nome_razao')
    trade_name = models.CharField(max_length=45, db_column='nome_fantasia')
    address = models.CharField(max_length=45, db_column='endereco')
    neighborhood = models.CharField(max_length=45, db_column='bairro')
    email = models.CharField(max_length=45)
    postal_code = models.CharField(max_length=45, db_column='cep')
    tax_id = models.CharField(max_length=45, db_column='cnpj')
    inep_code = models.CharField(max_length=45, db_column='inep')
    logo = models.TextField()
    additional_field = models.CharField(
        max_length=45, blank=True, null=True, db_column='escolascol',
    )

    class Meta:
        db_table = 'escolas'
        verbose_name = 'Escola'
        verbose_name_plural = 'Escolas'
