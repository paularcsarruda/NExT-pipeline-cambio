
import requests

url="https://servicodados.ibge.gov.br/api/v1/localidades/estados"
resposta = requests.get(url, timeout=10)
print("Status Code:", resposta.status_code) # passo 1: rodar e ver 200

estados = resposta.json() # passo 2: converter a resposta em JSON e armazenar na variável estados
print("Tipo:", type(estados)) # passo 3: rodar e ver que é uma lista
print("Quantidade de estados:", len(estados)) # passo 4: rodar e ver a quantidade de estados

# testes de impressão
# ver o primeiro estado
print(estados[0]) 

# estados do Nordeste
print("\nEstados do Nordeste:") 
for estado in estados:
    if estado['regiao']['sigla'] == 'N':
        print(f"{estado['nome']} - {estado['sigla']}")

