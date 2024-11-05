
from pyspark.sql import SparkSession
import os
import gcsfs
import pandas as pd

# Defina o caminho do arquivo de credenciais do Google Cloud
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/content/bees-440303-a4fa6e2ef5ea.json"

# Trago  do bucket e caminhos dos arquivos
bucket_name = "dev_bees"
csv_path = f"gs://{bucket_name}/camada_bronze/breweries.csv"

df = pd.read_csv(csv_path)

df.to_parquet(f"gs://{bucket_name}/camada_silver/breweries.parquet", partition_cols=['state_province'], index=False)
print("Dados transformados e particionados por estado na camada Silver")