"""
Example DAG demonstrating basic Airflow functionality.
This DAG runs daily and shows various operators and patterns.
"""

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from airflow.utils.task_group import TaskGroup

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
with DAG(
    'example_dag',
    default_args=default_args,
    description='A simple example DAG',
    schedule_interval='@daily',
    catchup=False,
    tags=['example', 'tutorial'],
) as dag:

    # Start and end tasks
    start = EmptyOperator(task_id='start')
    end = EmptyOperator(task_id='end')

    # Bash operator example
    print_date = BashOperator(
        task_id='print_date',
        bash_command='date',
    )

    # Python operator example
    def hello_world(**context):
        """Simple Python function that prints a message."""
        print("Hello from Airflow!")
        print(f"Execution date: {context['ds']}")
        return "Hello World executed successfully"

    hello_task = PythonOperator(
        task_id='hello_world',
        python_callable=hello_world,
    )

    # Another Python operator with parameters
    def process_data(name: str, value: int, **context):
        """Process some data and return a result."""
        result = f"Processing {name} with value {value}"
        print(result)
        return result

    process_task = PythonOperator(
        task_id='process_data',
        python_callable=process_data,
        op_kwargs={'name': 'sample_data', 'value': 42},
    )

    # Sleep task to simulate work
    sleep_task = BashOperator(
        task_id='sleep_task',
        bash_command='sleep 5 && echo "Slept for 5 seconds"',
    )

    # Task group example
    with TaskGroup(group_id='processing_group') as processing_group:
        task_a = BashOperator(
            task_id='task_a',
            bash_command='echo "Task A completed"',
        )

        task_b = BashOperator(
            task_id='task_b',
            bash_command='echo "Task B completed"',
        )

        task_c = BashOperator(
            task_id='task_c',
            bash_command='echo "Task C completed"',
        )

        # Task A and B run in parallel, then C runs after both
        [task_a, task_b] >> task_c

    # Define task dependencies
    start >> [print_date, hello_task] >> process_task >> sleep_task >> processing_group >> end