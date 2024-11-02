from django.core.management.base import BaseCommand

from weducar.apps.administration.models import ContractType


class Command(BaseCommand):
    help = 'Cria tipos de contrato'

    def handle(self, *args, **kwargs):
        contract_type = [
            'CLT',
            'CC',
            'Temporário',
            'Estágio',
        ]

        for description in contract_type:
            ContractType.objects.get_or_create(description=description)

        self.stdout.write(
            self.style.SUCCESS('Tipos de contrato criados com sucesso!'),
        )
