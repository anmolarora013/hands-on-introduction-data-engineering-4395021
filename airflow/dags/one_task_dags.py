"""One Task DAG"""
from datetime import datetime
from airflow.providers.standard.operators.bash import BashOperator
from airflow import DAG

default_args = {
    'owner': 'Anmol',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
}

with DAG(
    dag_id='one_task_dag',
    description='A simple one-task DAG',
    schedule=None,
    default_args=default_args,
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:

    task1 = BashOperator(
        task_id='one_task',
        bash_command='echo "hello, learning Airflow!" > /workspaces/hands-on-introduction-data-engineering-4395021/lab/temp/one_task_dag_output.txt',
    )
