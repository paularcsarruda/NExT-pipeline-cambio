
import requests

def consulta_viacep(cep):
    cep = cep.strip().replace("-", "")

    if not cep.isdigit() or len(cep) != 8:
        print("[erro] O CEP deve conter exatamente 8 números.")
        return None

    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()
    except requests.exceptions.Timeout:
        print(f"[erro] ViaCEP demorou demais. CEP: {cep}")
        return None
    except requests.exceptions.ConnectionError:
        print("[erro] Sem conexão ou servidor fora do ar.")
        return None
    except requests.exceptions.HTTPError as erro:
        print(f"[erro] Erro HTTP {resposta.status_code}: {erro}")
        return None

    dados = resposta.json()

    if dados.get("erro"):
        print(f"[erro] CEP não encontrado: {cep}")
        return None

    return dados


if __name__ == "__main__":
    cep = input("Digite o CEP: ")

    resultado = consulta_viacep(cep)

    if resultado:
        print(
            resultado["logradouro"],
            resultado["bairro"],
            resultado["localidade"],
            resultado["uf"],
            cep
        )