import pandas as pd
from azure.storage.blob import BlobServiceClient

TSV_FILE = "earthquakes.tsv"  
CSV_FILE = "earthquake_data.csv"  
AZURE_STORAGE_CONNECTION_STRING = ""  # Replace with your actual Azure connection string
CONTAINER_NAME = "earthquakedata"  # Replace with your Azure Blob Storage container name
BLOB_NAME = "projectazurekp450"


def convert_tsv_to_csv(tsv_file, csv_file):
    """Convert TSV file to CSV format."""
    try:
        df = pd.read_csv(tsv_file, sep="\t")  
        df.to_csv(csv_file, index=False) 
        print(f"✅ Conversion successful! File saved as: {csv_file}")
        return True
    except Exception as e:
        print(f"❌ Error during conversion: {e}")
        return False


def upload_to_azure_blob(csv_file, container_name, blob_name):
    """Upload CSV file to Azure Blob Storage."""
    try:
        blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

        with open(csv_file, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)

        print(f"✅ File uploaded successfully to Azure Blob Storage: {blob_name}")
    except Exception as e:
        print(f"❌ Error uploading file to Azure: {e}")

if __name__ == "__main__":
    if convert_tsv_to_csv(TSV_FILE, CSV_FILE):  # Convert first
        upload_to_azure_blob(CSV_FILE, CONTAINER_NAME, BLOB_NAME)  # Upload if conversion is successful
