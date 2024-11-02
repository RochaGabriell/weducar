from django.core.management.base import BaseCommand

from weducar.apps.administration.models import Position


class Command(BaseCommand):
    help = 'Cria cargos'

    def handle(self, *args, **kwargs):
        contract_type = [
            'Administrador(a)',
            'Diretor(a)',
            'Supervisor(a) de Ensino',
            'Coordenador(a) Pedagógico(a)',
            'Orientador(a) Pedágogico(a)',
            'Professor(a)',
            'Secretário(a) Escolar',
            'Auxiliar de Serviços Gerais',
            'Vígia',
        ]

        for description in contract_type:
            Position.objects.get_or_create(description=description)

        self.stdout.write(self.style.SUCCESS('Cargos criados com sucesso!'))
