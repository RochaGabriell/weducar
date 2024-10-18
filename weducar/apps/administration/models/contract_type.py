from django.db import models


class ContractType(models.Model):
    contract_type_id = models.AutoField(primary_key=True, db_column='id_tipo')
    description = models.CharField(max_length=45, db_column='descricao')

    class Meta:
        db_table = 'tipo_contrato'
        verbose_name = 'Tipo de contrato'
        verbose_name_plural = 'Tipos de contrato'
