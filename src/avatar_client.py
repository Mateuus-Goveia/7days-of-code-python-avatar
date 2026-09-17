import requests


class AvatarClient:

    def __init__(self):
        self.base_url = "https://last-airbender-api.fly.dev"

    def listar_personagens(self):
        url = f"{self.base_url}/api/v1/characters"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as err:
            print(f"Erro na requisição à API: {err}")
            return None

        