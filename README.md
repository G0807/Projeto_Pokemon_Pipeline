https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png

# ⚡ Pokémon Data Pipeline & Analytics

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Google Sheets](https://img.shields.io/badge/Google_Sheets-34A853?style=for-the-badge&logo=google-sheets&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

Este projeto é um pipeline de dados de ponta a ponta (ETL) que extrai informações da PokeAPI, organiza os dados estruturalmente e os carrega de forma automatizada no Google Sheets. Além disso, conta com um ambiente de análise exploratória de dados usando Pandas.

## 🏗️ Arquitetura do Projeto

O projeto foi dividido em duas grandes frentes: **Engenharia de Dados** e **Análise de Dados**.

### 1. Engenharia de Dados (ETL)
- **Extract:** Um script em Python consome a [PokeAPI](https://pokeapi.co/) para buscar os 100 Pokémon mais icônicos.
- **Transform:** Os dados JSON são tratados e normalizados em duas tabelas relacionais (Index e Stats) para evitar redundância.
- **Load:** Utilizando a biblioteca `gspread` e Google Cloud Service Accounts, os dados são carregados via API para o Google Sheets.
- **Automação:** O pipeline é executado automaticamente via **GitHub Actions** usando cron jobs, com gestão segura de credenciais via *GitHub Secrets*.

### 2. Análise Exploratória (Colab)
Os dados gerados pelo pipeline são consumidos diretamente do Google Sheets para um ambiente de análise.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/[(https://colab.research.google.com/drive/1wTp4ExjIK2ANY3GjPVdjOMkOt1YVKv0-?usp=sharing)])

No notebook, utilizamos a biblioteca **Pandas** para:
* Limpeza e cruzamento das abas (Merge).
* Criação de novas métricas (ex: *Power Index*).
* Ranqueamento dos atributos base (Velocidade, Ataque, Defesa).

## 🚀 Como visualizar os resultados
A planilha alimentada pelo robô pode ser visualizada estruturalmente. As abas estão divididas entre identificação em metadados (ID, Nome, Imagem) e dados estritamente numéricos para facilitar a análise estatística sem poluição visual.

 <img width="953" height="549" alt="Captura de Tela (68)" src="https://github.com/user-attachments/assets/266b842d-2088-41d7-b1c1-32c7d5ede774" />


## 🛠️ Como rodar o código de Engenharia localmente

1. Clone o repositório.
2. Instale as dependências: `pip install -r requirements.txt`.
3. Configure as suas credenciais do GCP no arquivo `.env` ou nas variáveis de ambiente.
4. Execute `python main.py`.

---
*Desenvolvido com foco em boas práticas, segurança de chaves em nuvem e análise de dados.*
