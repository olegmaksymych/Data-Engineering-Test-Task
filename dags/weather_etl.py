from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from src.extract import fetch_weather_data
from src.transform import transform_weather_data
from src.load import load_csv_psycopg2

def etl_task():
    raw_file = fetch_weather_data("Lviv", "2024-01-01", "2024-12-31")
    processed_file = transform_weather_data(raw_file)
    load_csv_psycopg2(processed_file)

with DAG(
    dag_id="weather_etl",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:
    run_etl = PythonOperator(
        task_id="run_etl_pipeline",
        python_callable=etl_task
    )
