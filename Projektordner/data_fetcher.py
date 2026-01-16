import os
import requests
from dotenv import load_dotenv

# Lädt Variablen aus der .env Datei
load_dotenv()

API_URL = "https://api.api-ninjas.com/v1/animals"
API_KEY = os.getenv("API_NINJAS_KEY")


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns a list of animal dictionaries.
    """
    if not API_KEY:
        raise RuntimeError("API_NINJAS_KEY nicht gefunden. Prüfe deine .env Datei.")

    response = requests.get(
        API_URL,
        params={"name": animal_name},
        headers={"X-Api-Key": API_KEY},
        timeout=20
    )
    response.raise_for_status()
    return response.json()