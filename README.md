
# Pipeline de Dados: PokeAPI para Google Sheets

Projeto de automação que extrai dados numéricos dos 100 Pokémon mais icônicos e os organiza em uma planilha estruturada para análise.

## 🚀 Tecnologias
* Python 3.x
* PokeAPI (Fonte de dados)
* Google Cloud Platform (APIs & Service Accounts)
* Bibliotecas: `requests`, `gspread`, `python-dotenv`

## 🛠️ Arquitetura do Projeto
O pipeline segue os princípios de **ETL (Extract, Transform, Load)**:
1. **Extract**: Busca dados brutos da PokeAPI.
2. **Transform**: Limpa e organiza os dados em duas categorias (Identificação e Atributos).
3. **Load**: Insere os dados via API nas abas correspondentes do Google Sheets.

## 🔐 Segurança e Boas Práticas
* Uso de **Service Accounts** para autenticação segura.
* Variáveis de ambiente (`.env`) para proteger IDs sensíveis.
* Tratamento de erros e logs para monitoramento do processo.
