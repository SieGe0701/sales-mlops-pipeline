from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
with DAG(
    dag_id='sales_prediction_retraining',
    default_args=default_args,
    description='Retrain Walmart sales prediction model daily',
    schedule_interval=timedelta(days=1),  # once every day
    start_date=datetime(2025, 4, 27),
    catchup=False,
    tags=['sales', 'ml', 'retraining'],
) as dag:

    # Define the task: run the training script
    retrain_model = BashOperator(
        task_id='retrain_model',
        bash_command='python /mlflow/train.py',  # Make sure the path matches inside your container
    )

retrain_model
    
