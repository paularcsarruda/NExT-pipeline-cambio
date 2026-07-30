
import json
from pathlib import Path

arquivos = sorted(Path("data/raw").glob("cotacoes_*.json")) # inicio do nome do arquivo = cotacoes_ + data + .json

print(arquivos)              # alfabetica = cronologica!

with open(arquivos[-1], encoding="utf-8") as f:  # [-1] -> mais recente
    dados = json.load(f)

print(type(dados))           # <class 'dict'>  (nao e lista!)
print(dados.keys())          # dict_keys(['USDBRL', 'EURBRL'])
print(dados["USDBRL"]["bid"])  # '5.43...'  string!