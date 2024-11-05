from pyspark.sql import SparkSession
import os
import gcsfs
import pandas as pd

# Defina o caminho do arquivo de credenciais do Google Cloud
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/content/bees-440303-a4fa6e2ef5ea.json"

# Trago  do bucket e caminhos dos arquivos
bucket_name = "dev_bees"
#csv_path = f"gs://{bucket_name}/camada_silver/breweries.parquet"

import pandas as pd

# Leitura dos dados da Camada Silver (formatados e particionados)
#df_silver = pd.read_parquet('gs://meu-data-lake/silver/breweries/')
df_silver = pd.read_parquet(f"gs://{bucket_name}/camada_silver/breweries.parquet")

# Agregação dos dados: Contagem de cervejarias por tipo e localização (estado)
df_gold = df_silver.groupby(['state', 'brewery_type']).size().reset_index(name='brewery_count')

# Salvando a visão agregada na Camada Gold
#df_gold.to_parquet(f"gs://{bucket_name}/camada_gold/breweries_aggregated/breweries_aggregated.parquet", index=False)
df_gold.to_csv(f"gs://{bucket_name}/camada_gold/breweries_aggregated/breweries_aggregated.csv", index=False)

print("Visão agregada criada e salva na Camada Gold!")