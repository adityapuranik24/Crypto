import faust
import pandas as pd
import sys
sys.path.extend([
    'D:/Projects/Crypto/Data',
    'D:/Projects/Crypto/Scripts/Excel',
    'D:/Projects/Crypto/Scripts/S3',
    'D:/Projects/Crypto/Scripts/Database',
    'D:/Projects/Crypto/Scripts/Calculations' ])
import Current_Date_Time as dt
# import MySQL_Connection as db_conn
import Loading_MySQL as lm
import Loading_MsSQL as ldb
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
    delta_quarter = []
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
        delta_quarter.append(message['delta']['quarter'])
        delta_year.append(message['delta']['year'])      

        # Getting current Date & Time
        timestamp, current_time, current_day, current_month_name, current_month, current_year, current_date_updated, current_hour = dt.current_date_time()           

        combined_data = pd.DataFrame(
                    { 'Time' : current_time, 
                    'Date': current_date_updated,
                    'Name': name,
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
                    'Delta_Quarter_Change' : delta_quarter,
                    'Delta_Year_Change' : delta_year,
                    'Hour' : current_hour,
                    'Day' : current_day,
                    'Month_Number': current_month,
                    'Month_Name' : current_month_name,
                    'Year' : current_year
                    })
        
        # Getting latest data in the form of pandas row
        combined_data = combined_data.tail(1)

        #Converting the columns in different datatypes 
        combined_data['Time'] = combined_data['Time'].astype('string')
        combined_data['Date'] = pd.to_datetime(combined_data['Date'], format='%Y-%m-%d')
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
        combined_data['Delta_Quarter_Change'] = combined_data['Delta_Quarter_Change'].astype('float') 
        combined_data['Delta_Year_Change'] = combined_data['Delta_Year_Change'].astype('float')  
        combined_data['Hour'] = combined_data['Hour'].astype('int') 
        combined_data['Day'] = combined_data['Day'].astype('int') 
        combined_data['Month_Number'] = combined_data['Month_Number'].astype('int')  
        combined_data['Month_Name'] = combined_data['Month_Name'].astype('string') 
        combined_data['Year'] = combined_data['Year'].astype('int')  

        # Creating a file for each entry with timestamp to save in S3 storge
        # current_time = datetime.datetime.now()
        file_name = f"market_{timestamp}.csv"
        with open('D:/Projects/Crypto/Data/FileName.py', 'w') as file:
            file.write(f"file_name = '{file_name}'\n")
        row_csv = combined_data.to_csv(index = False)

        # Establishing S3 connection
        s3_client = cc.get_connection()
        s3_client.put_object(Bucket=va.bucket_name, Key=file_name, Body=row_csv)
        ue.update_excel(combined_data)

        # Loading data on DataBase
        for row in combined_data.itertuples():
           # Sending data to MySQL Server
            lm.load_mysql(row)
            # Sending data to MsSQL Server
            ldb.load_mssql(row)
        print(combined_data)

if __name__ == '__main__':
   app.main()
        