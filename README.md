# Pipeline Cambio
Pepeline de dados do modulo M3 (NExT Dados 2026.1, Cesar School).
Coleta cotaçoes de cambio da Awesome API, guarda a camada raw, transforma com pandas e carrega em PostegreSQL e MongoDB Atlas.

## Como rodar
1. Criar e ativar o venv
2. pip install -r requirements.txt
3. python src/pipeline.py