# import bibliotecas
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
import requests
from config import OPENWEATHER_API_KEY

# url da API do OpenWeatherMap
url = "https://api.openweathermap.org/data/2.5/weather"

# solicita o nome da cidade ao usuário
cidade = input("Digite o nome da cidade: ")

# parâmetros da requisição
params = {"q": cidade, "appid": OPENWEATHER_API_KEY,
"units": "metric", "lang": "pt_br"}

resposta = requests.get(url, params=params, timeout=10)
resposta.raise_for_status()
clima = resposta.json()
print(f'{clima["name"]}: {clima["main"]["temp"]:.1f}C')