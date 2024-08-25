import boto3
from dotenv import load_dotenv
import os

load_dotenv()

def create_s3_client():
    s3_client = boto3.client(
        's3',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
    )

    return s3_client

def upload_to_s3():
    s3_client = create_s3_client()
    s3_client.upload_file('data/processed/ufc_data_prepared.csv', 'ufcprojectbucket', 'ufc_data_prepared.csv')

if __name__ == '__main__':
    upload_to_s3()