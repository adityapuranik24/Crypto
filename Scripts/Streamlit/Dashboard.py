import sys
import boto3 
import pandas as pd
from io import StringIO
sys.path.append('D:/Projects/Crypto/Scripts/Kafka')
sys.path.append('D:/Projects/Crypto/Data')
import Variables as va
import FileName as fn


def get_data():
    s3_client = boto3.client('s3', aws_access_key_id=va.aws_access_key_id, aws_secret_access_key=va.aws_secret_access_key)
    response = s3_client.get_object(Bucket=va.bucket_name, Key=fn.file_name)
    file_content = response['Body'].read().decode('utf-8')
    csv_data = pd.read_csv(StringIO(file_content))
    rate = csv_data.loc[0, 'Rate']
    # print(rate)
    return rate