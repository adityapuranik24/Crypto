import pandas as pd
from kafka import KafkaProducer
from time import sleep
from json import dumps
import sys
sys.path.append('D:/Projects/Crypto/Scripts/API')
import CoinsInfo as ce



def run_producer():
    data = ce.coin_info(0)
    producer = KafkaProducer(bootstrap_servers=['52.14.28.124:9092'],
                            value_serializer=lambda x: dumps(x).encode('utf-8'))

    producer.send('crypto', value=data)

while True:
    sleep(20)
    run_producer()