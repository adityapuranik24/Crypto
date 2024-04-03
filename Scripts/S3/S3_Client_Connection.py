import sys
import boto3 
sys.path.append('D:/Projects/Crypto/Data')
import Variables as va





def get_connection():
    s3_client = boto3.client('s3', aws_access_key_id=va.aws_access_key_id, aws_secret_access_key=va.aws_secret_access_key)
    return s3_client