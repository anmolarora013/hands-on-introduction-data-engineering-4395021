'''Load DAG'''
from datetime import datetime
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator

default_args = {
    'owner': 'Anmol',
    'description': 'A load DAG',
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0
}

with DAG(
    'load_dag',
    schedule= None,
    start_date=datetime(2025, 1, 1),
    default_args=default_args
) as dag:
    task = BashOperator(
        task_id='load_task',
        bash_command='echo -e ".separator ","\n.import --skip 1 /workspaces/hands-on-introduction-data-engineering-4395021/lab/orchestrated/airflow-extract-data.csv top_level_domains" | sqlite3 /workspaces/hands-on-introduction-data-engineering-4395021/lab/orchestrated/tld_database.db',
        dag=dag
    )