from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import sys, os

# Thêm đường dẫn chứa dự án ETL của bạn nếu cần
sys.path.insert(0, os.path.abspath('/d:/Project/Daily-Commute-Analytics-Recommendation'))

from scripts.etl_commute_pipeline import run_commute_etl

default_args = {
    'owner': 'your_name',
    'depends_on_past': False,
    'start_date': datetime(2025, 2, 1),
    'email': ['your_email@example.com'],
    'email_on_failure': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'daily_commute_etl',
    default_args=default_args,
    description='ETL Pipeline for Daily Commute Analytics & Recommendation using HERE Maps API',
    schedule_interval='0 6 * * *',  # Chạy lúc 6h sáng mỗi ngày
)

etl_task = PythonOperator(
    task_id='run_commute_etl',
    python_callable=run_commute_etl,
    dag=dag,
)
