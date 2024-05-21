import faust
import pandas as pd
import sys
import datetime
sys.path.append('D:/Projects/Crypto/Data')
sys.path.append('D:/Projects/Crypto/Scripts/Excel')
sys.path.append('D:/Projects/Crypto/Scripts/S3')
sys.path.append('D:/Projects/Crypto/Scripts/Database')
import MySQL_Connection as db_conn
import S3_Client_Connection as cc
import Updating_Excel as ue
import Variables as va





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
    delta_hour = []
    delta_day = []
    delta_week = []
    delta_month = []
    delta_year = []
    
    async for message in stream:
        rem_list = ['symbol', 'rank', 'color', 'png32', 'png64','webp32', 'webp64', 'pairs', 'categories', 'links']
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
        delta_hour.append(message['delta']['hour'])
        delta_day.append(message['delta']['day'])
        delta_week.append(message['delta']['week'])
        delta_month.append(message['delta']['month'])
        delta_year.append(message['delta']['year'])


        combined_data = pd.DataFrame(
                    {'Name': name,
                    'Age': age,
                    'Exchanges': exchanges,
                    'Markets': markets,
                    'All_Time_High' : alltimehigh,
                    'Circulating_Supply' : circulation,
                    'Total_Supply' : totalsupply,
                    'Max_Supply' : maxsupply,
                    'Rate' : rate,
                    'Volume' : volume,
                    'Cap' : cap,
                    'Liquidity' : liquidity,
                    'Delta_Hour_Change' : delta_hour,
                    'Delta_Day_Change' : delta_day,
                    'Delta_Week_Change' : delta_week,
                    'Delta_Month_Change' : delta_month,
                    'Delta_Year_Change' : delta_year
                    })
        
        combined_data = combined_data.tail(1)

        combined_data['Name'] = combined_data['Name'].astype('string')
        combined_data['Age'] = combined_data['Age'].astype('int')
        combined_data['Exchanges'] = combined_data['Exchanges'].astype('int')
        combined_data['Markets'] = combined_data['Markets'].astype('int')
        combined_data['All_Time_High'] = combined_data['All_Time_High'].astype('float')
        combined_data['Circulating_Supply'] = combined_data['Circulating_Supply'].astype('int64')
        combined_data['Total_Supply'] = combined_data['Total_Supply'].astype('int64')
        combined_data['Max_Supply'] = combined_data['Max_Supply'].astype('int64')
        combined_data['Rate'] = combined_data['Rate'].astype('float')
        combined_data['Volume'] = combined_data['Volume'].astype('int64')
        combined_data['Cap'] = combined_data['Cap'].astype('int64')
        combined_data['Liquidity'] = combined_data['Liquidity'].astype('int64')
        combined_data['Delta_Hour_Change'] = combined_data['Delta_Hour_Change'].astype('float')
        combined_data['Delta_Day_Change'] = combined_data['Delta_Day_Change'].astype('float')
        combined_data['Delta_Week_Change'] = combined_data['Delta_Week_Change'].astype('float')
        combined_data['Delta_Month_Change'] = combined_data['Delta_Month_Change'].astype('float')
        combined_data['Delta_Year_Change'] = combined_data['Delta_Year_Change'].astype('float')   


        current_time = datetime.datetime.now()
        file_name = f"market_{current_time}.csv"
        with open('D:/Projects/Crypto/Data/FileName.py', 'w') as file:
            file.write(f"file_name = '{file_name}'\n")
        row_csv = combined_data.to_csv(index = False)
        s3_client = cc.get_connection()
        s3_client.put_object(Bucket=va.bucket_name, Key=file_name, Body=row_csv)
        ue.update_excel(combined_data)
        cursor, db = db_conn.db_connect()
        # Select the database
        cursor.execute("USE CRYPTO")
        for row in combined_data.itertuples():
            cursor.execute('''
                    INSERT INTO BITCOIN (
                  Name, Age, Exchanges, Markets, All_Time_High, Circulating_Supply, Total_Supply,
                  Max_Supply, Rate, Volume, Cap, Liquidity, Delta_Hour_Change, Delta_Day_Change,
                  Delta_Week_Change, Delta_Month_Change, Delta_Year_Change) 
                  VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    ''',
                    (row.Name, 
                    row.Age,
                    row.Exchanges,
                    row.Markets, 
                    row.All_Time_High,
                    row.Circulating_Supply,
                    row.Total_Supply, 
                    row.Max_Supply,
                    row.Rate,
                    row.Volume, 
                    row.Cap,
                    row.Liquidity,
                    row.Delta_Hour_Change, 
                    row.Delta_Day_Change,
                    row.Delta_Week_Change,
                    row.Delta_Month_Change, 
                    row.Delta_Year_Change)
                )
            db.commit()
        print(combined_data)


        