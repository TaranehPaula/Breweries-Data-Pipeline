from airflow import DAG
from airflow import Dataset
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pandas as pd

mydataset = Dataset("/opt/airflow/data/breweries_aggregated_new.csv")

dag =  DAG('consumer', description="consumer",
        schedule=[mydataset],start_date=datetime(2024,11,4),
        catchup=False)

def my_file():
    dataset = pd.read_csv("/opt/airflow/data/breweries_aggregated.csv", sep=";")
    dataset.to_csv("/opt/airflow/data/breweries_aggregated_new2.csv", sep=";")

t1 = PythonOperator(task_id='t1', python_callable=my_file,dag=dag,provide_context=True)
t1