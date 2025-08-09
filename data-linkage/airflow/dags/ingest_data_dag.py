import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import timedelta

TZ = pendulum.timezone("Asia/Seoul")

def ingest_daily(**context):
    from data_ingestion import ingest
    ingest()

default_args = {
    "retries": 3,
    "retry_delay": timedelta(minutes=10),
}

with DAG(
    dag_id="ingestion_update",
    description="주기적으로 데이터 수집 실행",
    start_date=pendulum.datetime(2025, 8, 9, tz=TZ),
    schedule="0 3 * * *",  # 매일 새벽 3시
    catchup=False,
    default_args=default_args,
    tags=["data_ingestion"],
) as dag:

    PythonOperator(
        task_id="ingest_data_for_dworld",
        python_callable=ingest_daily,
        provide_context=True,
    )