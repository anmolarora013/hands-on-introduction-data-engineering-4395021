'''Extract DAG'''
from datetime import datetime
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator


default_args = {
    'owner': 'Anmol',
    'description': 'A extract DAG',
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0
}

with DAG(
    'extract_dag',
    schedule= None,
    start_date=datetime(2025, 1, 1),
    default_args=default_args
) as dag:
    task = BashOperator(
        task_id='extract_task',
        bash_command='wget -c https://datahub.io/core/top-level-domain-names/r/top-level-domain-names.csv.csv -O /workspaces/hands-on-introduction-data-engineering-4395021/lab/orchestrated/airflow-extract-data.csv'
    )
