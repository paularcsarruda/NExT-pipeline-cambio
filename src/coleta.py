import json
from datetime import datetime, timezone
from pathlib import Path
import requests

URL = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL"
# Diretório para armazenar os dados brutos
RAW_DIR = Path("data/raw")

def coletar_cotacoes () -> dict:
    resposta = requests.get(URL, timeout=10)
    resposta.raise_for_status()
    return resposta.json()

cotacoes = coletar_cotacoes()
print(cotacoes)

def salvar_raw(dados:dict) -> Path:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    arquivo = RAW_DIR / f"cotacoes_{timestamp}.json"
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)
    return arquivo

if __name__ == "__main__":
    arquivo = salvar_raw(coletar_cotacoes())
    print(f"Arquivo RAW salvo em: {arquivo}")