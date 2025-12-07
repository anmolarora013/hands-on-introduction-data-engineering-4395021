"""Two task DAG"""
from datetime import datetime
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator

default_args = {
    'owner': 'Anmol',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
}

with DAG(
    dag_id='two_task_dag',
    description='A two task Airflow DAG',
    schedule=None,                   # manual only
    default_args=default_args,
    start_date=datetime(2023, 1, 1), # put start_date here (cleaner)
    catchup=False,
) as dag:

    task0 = BashOperator(
        task_id='bash_task_0',
        bash_command='echo "This is task 0"',
    )

    task1 = BashOperator(
        task_id='bash_task_1',
        bash_command='echo "This is task 1" && sleep 5 && echo "Good Morning!"',
    )

    task0 >> task1
