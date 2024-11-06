from django.core.management.base import BaseCommand
from weducar.apps.students.models import Color


class Command(BaseCommand):
    help = 'Cria as cores para o aluno'

    def handle(self, *args, **kwargs):
        colors = [
            'Parda',
            'Negra',
            'Branca',
            'Indígena',
            'Amarela',
            'Não Declarada'
        ]

        for description in colors:
            Color.objects.get_or_create(description=description)

        self.stdout.write(self.style.SUCCESS('Cores criadas com sucesso!'))
