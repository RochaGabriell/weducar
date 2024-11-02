from django.core.management.base import BaseCommand

from weducar.apps.students.models import StudentStatus


class Command(BaseCommand):
    help = 'Cria situações do aluno'

    def handle(self, *args, **kwargs):
        contract_type = [
            'Ativo',
            'Inativo',
            'Desistente',
            'Transferido',
            'Cursando',
            'Falecido',
        ]

        for description in contract_type:
            StudentStatus.objects.get_or_create(description=description)

        self.stdout.write(
            self.style.SUCCESS('Situações do aluno criados com sucesso!'),
        )
