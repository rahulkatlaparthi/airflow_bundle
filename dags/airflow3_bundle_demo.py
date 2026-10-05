from datetime import datetime

from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator


def hello_airflow():
    print("Hello from Airflow 3 Git Bundle!")
    print("GitHub -> Bundle -> DAG Processor -> Scheduler")


with DAG(
    dag_id="airflow3_bundle_demo",
    start_date=datetime(2026, 10, 1),
    schedule=None,
    catchup=False,
    tags=["bundle", "gcp", "learning"],
) as dag:

    hello = PythonOperator(
        task_id="hello_airflow",
        python_callable=hello_airflow,
    )
