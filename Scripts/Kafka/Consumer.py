import faust
import pandas as pd
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
        combined_data.to_csv("D:/Projects/Crypto/Cleaned Data/sample_data.csv", index = False)