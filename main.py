import os
import json
import requests
import gspread
import time
import logging
from google.oauth2.service_account import Credentials

# Configuração de Logs
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PokemonPipeline:
    def __init__(self):
        self.base_url = "https://pokeapi.co/api/v2/pokemon/"
        self.spreadsheet_id = os.getenv("SPREADSHEET_ID")
        self.scopes = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]
        
        # Lógica para autenticação (GitHub Secrets ou Local)
        creds_json = os.getenv("GOOGLE_CREDENTIALS")
        if creds_json:
            # No GitHub Actions, o segredo é uma string JSON
            info = json.loads(creds_json)
            self.creds = Credentials.from_service_account_info(info, scopes=self.scopes)
        else:
            # Localmente, usa o arquivo
            self.creds = Credentials.from_service_account_file("credentials.json", scopes=self.scopes)
            
        self.client = gspread.authorize(self.creds)
        self.sheet = self.client.open_by_key(self.spreadsheet_id)

    def fetch_pokemon_data(self, pokemon_id):
        try:
            response = requests.get(f"{self.base_url}{pokemon_id}", timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logging.error(f"Erro ao buscar Pokemon {pokemon_id}: {e}")
            return None

    def run(self, limit=100):
        index_list = []
        stats_list = []
        
        logging.info(f"Iniciando extração de {limit} Pokemons...")
        
        for i in range(1, limit + 1):
            raw_data = self.fetch_pokemon_data(i)
            if raw_data:
                # Dados Identificação
                index_list.append([raw_data['id'], raw_data['name'], raw_data['sprites']['front_default']])
                
                # Dados Numéricos
                stats_dict = {s['stat']['name']: s['base_stat'] for s in raw_data['stats']}
                stats_list.append([
                    raw_data['id'], stats_dict.get('hp'), stats_dict.get('attack'), 
                    stats_dict.get('defense'), stats_dict.get('special-attack'), 
                    stats_dict.get('special-defense'), stats_dict.get('speed'),
                    raw_data['height'], raw_data['weight'], raw_data['base_experience']
                ])
                time.sleep(0.1)

        try:
            # Limpa e atualiza a aba Index
            ws_index = self.sheet.worksheet("Pokemon_Index")
            ws_index.clear()
            ws_index.append_row(["ID", "Nome", "URL_Imagem"])
            ws_index.append_rows(index_list)

            # Limpa e atualiza a aba Stats
            ws_stats = self.sheet.worksheet("Stats")
            ws_stats.clear()
            ws_stats.append_row(["ID", "HP", "Attack", "Defense", "Special-Attack", "Special-Defense", "Speed", "Height", "Weight", "Base_Experience"])
            ws_stats.append_rows(stats_list)
            
            logging.info("Pipeline concluído com sucesso!")
        except Exception as e:
            logging.error(f"Erro ao salvar no Google Sheets: {e}")

if __name__ == "__main__":
    pipeline = PokemonPipeline()
    pipeline.run(limit=100)
