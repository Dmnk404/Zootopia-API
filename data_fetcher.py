import os
import requests
from dotenv import load_dotenv

load_dotenv()

def fetch_data(animal_name):
  """
  Fetches the animals data for the animal 'animal_name'.
  Returns: a list of animals, each animal is a dictionary:
  {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
  },
  """

  api_key = os.getenv("API_KEY")
  if not api_key:
      raise ValueError("API_KEY not found. Please set it in .env file.")

  url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
  headers = {
      "X-Api-Key": api_key
  }

  response = requests.get(url, headers=headers)
  response.raise_for_status()

  return response.json()

