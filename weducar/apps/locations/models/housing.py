from django.db import models


class Housing(models.Model):
    housing_id = models.AutoField(
        primary_key=True, verbose_name='ID da Moradia', db_column='id_moradia',
    )
    description = models.CharField(
        max_length=255, verbose_name='Descrição', db_column='descricao',
    )

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'moradia'
        verbose_name = 'Moradia'
        verbose_name_plural = 'Moradias'
