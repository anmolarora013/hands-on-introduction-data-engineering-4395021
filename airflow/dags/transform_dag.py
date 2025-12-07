'''Transform DAG'''
from datetime import datetime,date
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
import pandas as pd

default_args = {
    'owner': 'Anmol',
    'description': 'A transform DAG',
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0
}

with DAG(
    'transform_dag',
    schedule= None,
    start_date=datetime(2025, 1, 1),
    default_args=default_args
) as dag:
    
    def transform_data():
        """Read in the file and transformed file out"""

        df = pd.read_csv('/workspaces/hands-on-introduction-data-engineering-4395021/lab/orchestrated/airflow-extract-data.csv')

        generic_type_df = df[df['Type'] == 'generic']
        generic_type_df['Date'] = date.today().strftime('%Y-%m-%d')
        generic_type_df.to_csv('/workspaces/hands-on-introduction-data-engineering-4395021/lab/orchestrated/airflow-transform-data.csv', index=False)
    
    task = PythonOperator(
        task_id='transform_task',
        python_callable=transform_data,
        dag=dag
    )