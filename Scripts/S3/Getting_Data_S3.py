import sys
import pandas as pd
from io import StringIO
sys.path.append('D:/Projects/Crypto/Scripts/Kafka')
sys.path.append('D:/Projects/Crypto/Data')
sys.path.append('D:/Projects/Crypto/Scripts/S3')
import S3_Client_Connection as cc
import Variables as va
import FileName as fn





def get_data(data):
    s3_client = cc.get_connection()
    response = s3_client.get_object(Bucket=va.bucket_name, Key=fn.file_name)
    file_content = response['Body'].read().decode('utf-8')
    csv_data = pd.read_csv(StringIO(file_content))
    fetched_data = csv_data.loc[0, f'{data}']
    return fetched_data
