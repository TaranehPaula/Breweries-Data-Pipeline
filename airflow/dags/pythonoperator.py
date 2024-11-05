from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import statistics as sts

dag =  DAG('pythonoperator', description="pythonoperator",
        schedule_interval=None,start_date=datetime(2024,11,4),
        catchup=False)

def data_cleaner():
   dataset = pd.read_csv("/opt/airflow/data/breweries_aggregated.csv", sep=";") 
   dataset.columns = ["state","brewery_type","brewery_count"]
      
   dataset.drop_duplicates(subset=["state","brewery_type"], keep="first", inplace=True)

   dataset.to_csv("/opt/airflow/data/breweries_aggregated_clean.csv", sep=";", index=False)

t1 = PythonOperator(task_id='t1', python_callable=data_cleaner, dag=dag)

t1
