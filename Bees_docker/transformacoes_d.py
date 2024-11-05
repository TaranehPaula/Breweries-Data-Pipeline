# %pip install google-cloud-storage

from pyspark.sql import SparkSession
import os
import gcsfs
import pandas as pd
import pyarrow

# Defina o caminho do arquivo de credenciais do Google Cloud
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/app/bees-440303-a4fa6e2ef5ea.json"

# Trago  do bucket e caminhos dos arquivos
bucket_name = "dev_bees"
csv_path = f"gs://{bucket_name}/camada_bronze/breweries_d.csv"

df = pd.read_csv(csv_path)

df.to_parquet(f"gs://{bucket_name}/camada_silver/breweries_d.parquet", partition_cols=['state_province'], index=False)
print("Dados transformados e particionados por estado na camada Silver")