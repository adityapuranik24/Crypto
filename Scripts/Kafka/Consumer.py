from kafka import KafkaConsumer
from time import sleep
from json import dumps,loads
import json
#from s3fs import S3FileSystem


consumer = KafkaConsumer('crypto', bootstrap_servers=['3.17.23.28:9092'],
           value_deserializer=lambda x: loads(x.decode('utf-8')))


for c in consumer:
    print(c.value)