import pandas as pd
from kafka import KafkaProducer
from time import sleep
from json import dumps
import json
import API



data = API.coin_info(0)
print(data)


# producer = KafkaProducer(bootstrap_servers=['3.17.23.28:9092'],
#                          value_serializer=lambda x: dumps(x).encode('utf-8'))


# data = {'surnasdasdame':'parasdasdmar'}
# producer.send('demo_test', value=data)
