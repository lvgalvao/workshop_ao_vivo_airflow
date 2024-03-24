from time import sleep

from airflow.decorators import dag, task

from datetime import datetime


@dag(
        dag_id="minha_quinta_pipeline",
        description="minha etl braba",
        schedule="* * * * *",
        start_date=datetime(2023,3,24),
        catchup=False #backfill
)
def minha_quinta_pipeline():

    @task
    def primeira_atividade():
        print("minha primeira atividade! - Hello World")
        sleep(2)

    @task
    def segunda_atividade():
        print("minha segunda atividade! - Hello World")
        sleep(2)
    
    @task
    def terceira_atividade():
        print("minha terceira atividade - Hello World")
        sleep(2)

    @task
    def quarta_atividade():
        print("pipeline finalizou")   

    t1 = primeira_atividade()
    t2 = segunda_atividade()
    t3 = terceira_atividade()
    t4 = quarta_atividade()

    t1.set_downstream([t2, t3])
    t3.set_upstream(t4)

minha_quinta_pipeline()