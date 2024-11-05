from airflow import DAG
from airflow import Dataset
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pandas as pd


dag =  DAG('producer', description="producer",
        schedule_interval=None,start_date=datetime(2024,11,4),
        catchup=False)

mydataset = Dataset("/opt/airflow/data/breweries_aggregated_new.csv")

def my_file():
    dataset = pd.read_csv("/opt/airflow/data/breweries_aggregated.csv", sep=";")
    dataset.to_csv("/opt/airflow/data/reweries_aggregated_new.csv", sep=";")

t1 = PythonOperator(task_id='t1', python_callable=my_file,dag=dag,outlets=[mydataset])
t1



