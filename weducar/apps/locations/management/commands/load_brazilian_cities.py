import requests
from django.core.management.base import BaseCommand
from ...models import State, City


class Command(BaseCommand):
    help = "Adiciona estados e cidades do Brasil ao banco de dados"

    def handle(self, *args, **options):
        states_url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"

        response = requests.get(states_url)
        states_data = response.json()

        for state_data in states_data:
            state, created = State.objects.get_or_create(
                uf=state_data['sigla'],
                defaults={'name': state_data['nome']}
            )

            self.stdout.write(f"Estado adicionado: {state.name}")

            cities_url = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{
                state.uf}/municipios"

            cities_response = requests.get(cities_url)
            cities_data = cities_response.json()

            for city_data in cities_data:
                City.objects.create(
                    state=state,
                    name=city_data['nome']
                )

                self.stdout.write(
                    f"Cidade adicionada: {city_data['nome']} - {state.uf}"
                )

        self.stdout.write(self.style.SUCCESS("Dados carregados com sucesso!"))
