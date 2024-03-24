import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator

minha_dag = DAG(
    dag_id="meu_nome_de_dag",
    start_date=datetime.datetime(2024, 3, 23),
    schedule="@daily",
    catchup=False,  # Adiciona esta linha
)
EmptyOperator(task_id="tarefa", dag=minha_dag)