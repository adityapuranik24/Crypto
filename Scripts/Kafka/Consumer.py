import faust
import pandas as pd
import boto3
import sys
sys.path.append('D:/Projects/Crypto/Data')
sys.path.append('D:/Projects/Crypto/Scripts/Excel')
import Updating_Excel as ue
import Variables as va
import datetime




app=faust.App('demo-streaming',broker='kafka://52.14.28.124:9092')

input_topic = app.topic('crypto', value_serializer='json')

@app.agent(input_topic)
async def processor(stream):
    
    name = []
    age = []
    exchanges = []
    markets = []
    alltimehigh = []
    circulation = []
    totalsupply = []
    maxsupply = []
    rate = []
    volume = []
    cap = []
    liquidity = []
    async for message in stream:
        rem_list = ['symbol', 'rank', 'color', 'png32', 'png64','webp32', 'webp64', 'pairs', 'categories', 'links', 'delta']
        for key in rem_list:
            del message[key]
        name.append(message['name'])
        age.append(message['age'])
        exchanges.append(message['exchanges'])
        markets.append(message['markets'])
        alltimehigh.append(message['allTimeHighUSD'])
        circulation.append(message['circulatingSupply'])
        totalsupply.append(message['totalSupply'])
        maxsupply.append(message['maxSupply'])
        rate.append(message['rate'])
        volume.append(message['volume'])
        cap.append(message['cap'])
        liquidity.append(message['liquidity'])

        combined_data = pd.DataFrame(
                    {'Name': name,
                    'Age': age,
                    'Exchanges': exchanges,
                    'Markets': markets,
                    'All Time High' : alltimehigh,
                    'Circulating Supply' : circulation,
                    'Total Supply' : totalsupply,
                    'Max Supply' : maxsupply,
                    'Rate' : rate,
                    'Volume' : volume,
                    'Cap' : cap,
                    'Liquidity' : liquidity
                    })
        
        combined_data = combined_data.tail(1)
        current_time = datetime.datetime.now()
        file_name = f"market_{current_time}.csv"
        with open('D:/Projects/Crypto/Data/FileName.py', 'w') as file:
            file.write(f"file_name = '{file_name}'\n")
        row_csv = combined_data.to_csv(index = False)
        s3_client = boto3.client('s3', aws_access_key_id=va.aws_access_key_id, aws_secret_access_key=va.aws_secret_access_key)
        s3_client.put_object(Bucket=va.bucket_name, Key=file_name, Body=row_csv)
        ue.update_excel(combined_data)
        print(combined_data)


        