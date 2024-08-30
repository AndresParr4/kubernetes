from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2020, 1, 1),
    'catchup': False,
    
}

with DAG('holamundo', default_args=default_args, schedule_interval='@daily') as dag:
    t1 = BashOperator(
        task_id='print_date',
        bash_command='date',
    )

    t2 = BashOperator(
        task_id='sleep',
        bash_command='echo "Hola Mundo"',
        dag=dag
    )

    t1 >> t2
