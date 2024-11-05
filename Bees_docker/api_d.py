import requests
import pandas as pd
import io
import os

from google.cloud import bigquery, storage

"""## GET URL"""

url = "https://api.openbrewerydb.org/v1/breweries"

resultados = []

try:
    # Realiza a requisição à API
    response = requests.get(url)
    response.raise_for_status()

    # Converte o conteúdo da resposta para JSON
    breweries_data = response.json()

    # Itera sobre cada item e estrutura no formato desejado
    for brewery in breweries_data:
        resultado = {
            "id": brewery.get("id"),
            "name": brewery.get("name"),
            "brewery_type": brewery.get("brewery_type"),
            "address_1": brewery.get("address_1"),
            "address_2": brewery.get("address_2"),
            "address_3": brewery.get("address_3"),
            "city": brewery.get("city"),
            "state_province": brewery.get("state_province"),
            "postal_code": brewery.get("postal_code"),
            "country": brewery.get("country"),
            "longitude": brewery.get("longitude"),
            "latitude": brewery.get("latitude"),
            "phone": brewery.get("phone"),
            "website_url": brewery.get("website_url"),
            "state": brewery.get("state"),
            "street": brewery.get("street")
        }
        resultados.append(resultado)

except requests.RequestException as e:
    print(f"Erro ao acessar a API: {e}")

# Converte a lista de dicionários em um DataFrame
df_resultados = pd.DataFrame(resultados)

num_linhas = len(df_resultados)
print(f"Quantidade de linhas: {num_linhas}")

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/app/bees-440303-a4fa6e2ef5ea.json"

client = bigquery.Client()
bucket_name = "dev_bees"
bucket = storage.Client().bucket(bucket_name)

# Define o caminho do arquivo dentro do bucket
blob = bucket.blob("camada_bronze/breweries_d.csv")

# Salva os dados no bucket
blob.upload_from_string(df_resultados.to_csv(index=False), content_type="text/csv")