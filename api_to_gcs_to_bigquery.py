import pandas as pd
import yaml
from sodapy import Socrata
from pathlib import Path
from google.cloud import storage
from google.cloud import bigquery


with open('config.yaml') as f:
    config = yaml.safe_load(f)


app_token = config['app_token']
username = config['username']
password = config['password']

def auth(app_token, username, password):
    # authenticated client (needed for non-public datasets):
    api_client = Socrata("data.lacity.org", app_token, username=username, password=password)
    return api_client

def extract_data(api_client, limit, offset):
    # results returned as JSON from API / converted to Python list of dictionaries by sodapy.
    results = api_client.get("wjz9-h9np", limit=limit, offset=offset)

    # Convert to pandas DataFrame
    results_df = pd.DataFrame.from_records(results)

    return results_df

def write_local(df: pd.DataFrame)->Path:
    path=Path("citation_data.parquet")
    df.to_parquet(path,compression="gzip")
    return path

def write_gcs(path):
    # GCS bucket name and destination object name
    bucket_name = "lucky_parking_bucket"
    destination_blob_name = str(path)

    # Initialize the GCS client
    storage_client = storage.Client()

    # Get the bucket
    bucket = storage_client.get_bucket(bucket_name)

    # Upload the Parquet file to GCS
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(path)

    print(f"Parquet file {path} uploaded to {destination_blob_name} in {bucket_name}")

    # return blob


def bigquery_table():

    bigquery_client = bigquery.Client(project="celtic-surface-388300")


    # TODO(developer): Set table_id to the ID of the table to create.
    table_id = "celtic-surface-388300.luckyparking_dataset.parking"

    job_config = bigquery.LoadJobConfig( write_disposition=bigquery.WriteDisposition.WRITE_APPEND, source_format=bigquery.SourceFormat.PARQUET,)
    uri = "gs://lucky_parking_bucket/citation_data.parquet"

    load_job = bigquery_client.load_table_from_uri(uri, table_id, job_config=job_config) # Make an API request.

    load_job.result() # Waits for the job to complete.

    destination_table = bigquery_client.get_table(table_id)
    print("Loaded {} rows.".format(destination_table.num_rows))


def api_to_bigquery() -> None:
    """The main ETL function"""
    limit = 1000000
    offset= 1000000
    api_client = auth(app_token, username, password)
    for i in range(0,17):
        df = extract_data(api_client, limit, i*offset)
        path = write_local(df)
        write_gcs(path)
        bigquery_table()


if __name__ == "__main__":
    api_to_bigquery()