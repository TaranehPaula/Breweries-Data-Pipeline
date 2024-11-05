import os
import gcsfs
import pandas as pd
from google.cloud import bigquery, storage  # Importação do cliente BigQuery e Storage

# Defina o caminho do arquivo de credenciais do Google Cloud
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/app/bees-440303-a4fa6e2ef5ea.json"

# Inicializa o cliente GCS e BigQuery
fs = gcsfs.GCSFileSystem()
client = bigquery.Client()
storage_client = storage.Client()

bucket_name = "dev_bees"

# Leitura dos dados da Camada Bronze
parquet_path = f"gs://{bucket_name}/camada_silver/breweries.parquet"
df_bronze = pd.read_csv(fs.open(parquet_path))

# Agregação dos dados: Contagem de cervejarias por tipo e localização (estado)
df_gold = df_bronze.groupby(['state', 'brewery_type']).size().reset_index(name='brewery_count')

# Caminho para salvar o arquivo na Camada Gold
csv_save_path = f"gs://{bucket_name}/camada_gold/breweries_aggregated/breweries_aggregated_d.csv"

# Salvando a visão agregada na Camada Gold
with fs.open(csv_save_path, 'w') as f:
    df_gold.to_csv(f, index=False)

print("Dados agregados salvos na Camada Gold como CSV.")

# Define o bucket e o caminho do blob dentro do bucket
bucket = storage_client.bucket(bucket_name)
blob = bucket.blob("camada_bronze/breweries_d.csv")

# Salva os dados agregados no bucket
blob.upload_from_string(df_gold.to_csv(index=False), content_type="text/csv")
