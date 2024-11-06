from django.db import models


class Color(models.Model):
    description = models.CharField(
        max_length=50, unique=True, verbose_name="Descrição da Cor",
        db_column='descricao'
    )

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'cor'
        verbose_name = 'Cor'
        verbose_name_plural = 'Cores'
