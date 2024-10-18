from django.core.management.base import BaseCommand

from weducar.apps.administration.models import Schooling


class Command(BaseCommand):
    help = 'Cria níveis de escolaridade padrão'

    def handle(self, *args, **kwargs):
        schooling_levels = [
            "Ensino Fundamental Completo",
            "Ensino Fundamental Incompleto",
            "Ensino Médio Completo",
            "Ensino Médio Incompleto",
            "Ensino Pós Graduação Completo",
            "Ensino Pós Graduação Incompleto",
            "Ensino Superior Completo",
            "Ensino Superior Incompleto",
        ]

        for description in schooling_levels:
            Schooling.objects.get_or_create(description=description)

        self.stdout.write(
            self.style.SUCCESS('Níveis de escolaridade criados com sucesso!'),
        )
