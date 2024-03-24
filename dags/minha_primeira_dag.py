import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="meu_nome_de_dag",
    start_date=datetime.datetime(2021, 1, 1),
    schedule="@daily",
    catchup=False
):
    EmptyOperator(task_id="tarefa")