"""
In this module a python callable is created, that when it runs, it ETLs data in bigquery.
Moreover a DAG is defined that can be used to run tasks in airflow.
In the DAG one taks is created.This task executes the python callable that is defined whenever it is triggered.
"""

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os
from google.cloud import bigquery

# import defined functions
from functions.transform_raw_data import transform_data
from functions.table_schema import subscriptions_schema


def _batch_load_data_in_bigquery():
    """
    This function is used in order to ETL data into a bigquery.
    More specifically, firstly it extracts data from a json file. The url of the file needs to be defined.
    Then it transform the data in the required newline delimited json format that is required from bigquery.
    Afterwards, it creates the desired table in bigquery. The table_id needs to be set.
    Finally, it will load the transformed data contained in the created table.
    To be noted that the google credentials must also be provided.
    Args:
    Returns:
    """

    # Url with the json in github
    url = "https://raw.githubusercontent.com/TomSouliot/Test_connection/main/etl.json"
    
    # Use the created function to make the required transformations in the extracted file
    payload_as_file = transform_data(url)

    # Provide google credentials
    credential_path = "./dags/ae-ts-assignment-16d810bb743b.json"
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

    # Construct a BigQuery client object
    client = bigquery.Client()

    # Use the created function in order to define the schema of the table to be created
    table_schema = subscriptions_schema()

    # Define the table_id. The schema is "staging" and the table created will be "raw_subscriptions"
    table_id = "ae-ts-assignment.staging.raw_subscriptions"

    # Make a request to create the table
    table = bigquery.Table(table_id, schema=table_schema)
    table = client.create_table(table) 
    print(
        "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
    )

    # Make a request to load the data in the table    
    job_config = bigquery.LoadJobConfig()
    job_config.source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON
    job = client.load_table_from_file(payload_as_file, table_id, job_config = job_config)
    print(job.result())
        

# Define the DAG that can be used to run the function that ETLs data in bigquery
with DAG("batch_load_bigquery", start_date = datetime(2023, 12, 1),
         schedule_interval = "@yearly", catchup = False) as dag:
    
        # Define a task that calls the python function to ETL data in bigquery
        bigquery_batch_load = PythonOperator(
                task_id = "bigquery_load_data",
                python_callable = _batch_load_data_in_bigquery
        )


