import requests
from random import randint

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

def random_pokemon():
    try:
        pokemon_id = randint(1, 1025)
        response = requests.get(f"{BASE_URL}{pokemon_id}", timeout=5)
        response.raise_for_status()

        data = response.json()

        types = [t["type"]["name"] for t in data["types"]]

        pokemon = {
            "name": data["name"],
            "types": types if len(types) > 1 else types * 2
        }

        return pokemon

    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")

    except KeyError:
        print("Erro ao processar os dados da API")

random_pokemon()
