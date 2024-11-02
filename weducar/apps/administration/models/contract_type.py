from django.db import models


class ContractType(models.Model):
    contract_type_id = models.AutoField(
        primary_key=True, verbose_name='ID do Tipo', db_column='id_tipo',
    )
    description = models.CharField(
        max_length=45, verbose_name='Descrição', db_column='descricao',
    )
    
    def __str__(self):
        return self.description

    class Meta:
        db_table = 'tipo_contrato'
        verbose_name = 'Tipo de contrato'
        verbose_name_plural = 'Tipos de contrato'
