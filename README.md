<h1 align="center"> Pipeline de Câmbio</h1>

<p align="center">Pipeline de dados desenvolvido durante o Módulo 3 do programa NExT Dados 2026.1, da CESAR School.</p>

## Objetivo

O objetivo do projeto é aplicar, de forma prática, as principais etapas de um pipeline de dados:

1. Extração de dados de uma API externa;
2. Armazenamento dos dados brutos;
3. Limpeza e transformação dos dados;
4. Carregamento em bancos de dados relacionais e não relacionais.

## Tecnologias utilizadas

* Python
* Pandas
* Requests
* PostgreSQL
* SQLAlchemy
* MongoDB Atlas
* PyMongo
* Git e GitHub

## Fluxo do pipeline

```text
AwesomeAPI
    ↓
Coleta das cotações
    ↓
Camada Raw
    ↓
Transformação com Pandas
    ↓
PostgreSQL e MongoDB Atlas
```

## Estrutura do projeto

```text
pipeline-cambio/
├── data/
│   └── raw/
├── src/
│   └── pipeline.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Como executar

### 1. Clone o repositório

```bash
git clone URL_DO_REPOSITORIO
cd pipeline-cambio
```

### 2. Crie o ambiente virtual

```bash
python3 -m venv .venv
```

### 3. Ative o ambiente virtual

No macOS ou Linux:

```bash
source .venv/bin/activate
```

No Windows:

```bash
.venv\Scripts\activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Configure as conexões

Configure as credenciais necessárias para conexão com o PostgreSQL e o MongoDB Atlas.

Por segurança, informações como usuário, senha e endereço dos bancos não devem ser adicionadas diretamente ao código nem enviadas ao GitHub.

### 6. Execute o pipeline

```bash
python src/pipeline.py
```

## Etapas realizadas

### Extração

As cotações de câmbio são coletadas por meio da API pública da AwesomeAPI.

### Armazenamento Raw

Os dados retornados pela API são armazenados sem alterações, preservando o formato original da fonte.

### Transformação

Os dados são processados com Pandas, incluindo operações como:

* seleção de campos relevantes;
* conversão de tipos;
* tratamento de valores;
* organização das colunas;
* preparação dos dados para armazenamento.

### Carregamento

Após o tratamento, os dados são carregados em dois tipos de banco:

* **PostgreSQL**, representando o armazenamento relacional;
* **MongoDB Atlas**, representando o armazenamento orientado a documentos.

## Status

Projeto acadêmico em desenvolvimento.

Desenvolvido por **Paula Roberta Arruda** durante o programa **NExT Dados 2026.1**, da CESAR School.
