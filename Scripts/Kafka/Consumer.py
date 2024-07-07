import faust
import pandas as pd
import sys
sys.path.extend([
    'D:/Projects/Crypto-Develop/Crypto-Develop/Data',
    'D:/Projects/Crypto-Develop/Crypto-Develop/Scripts/Excel',
    'D:/Projects/Crypto-Develop/Crypto-Develop/Scripts/S3',
    'D:/Projects/Crypto-Develop/Crypto-Develop/Scripts/Database',
    'D:/Projects/Crypto-Develop/Crypto-Develop/Scripts/Calculations' ])
import Current_Date_Time as dt
import MySQL_Connection as db_conn
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
    rank = []
    age = []
    exchanges = []
    markets = []
    pairs = []
    # categories = []
    alltimehigh = []
    circulation = []
    totalsupply = []
    maxsupply = []
    code = []
    rate = []
    volume = []
    cap = []
    # liquidity = []
    delta_hour = []
    delta_day = []
    delta_week = []
    delta_month = []
    delta_quarter = []
    delta_year = []
    
    async for message in stream:
        value = []
        length = len(message)
        for i in range (0,length):
          value = message[i]
          rem_list = ['symbol', 'color', 'png32','png64','webp32', 'categories', 'webp64', 'links', ]
          for key in rem_list:
            if key in value:
              del value[key]
          if value['maxSupply'] is None:
            value['maxSupply'] = 000
          name.append(value['name'])
          rank.append(value['rank'])
          age.append(value['age'])
          exchanges.append(value['exchanges'])
          markets.append(value['markets'])
          pairs.append(value['pairs'])
          alltimehigh.append(value['allTimeHighUSD'])
          circulation.append(value['circulatingSupply'])
          totalsupply.append(value['totalSupply'])
          maxsupply.append(value['maxSupply'])
          code.append(value['code'])
          rate.append(value['rate'])
          volume.append(value['volume'])
          cap.append(value['cap'])
          # liquidity.append(message['liquidity'])
          delta_hour.append(value['delta']['hour'])
          delta_day.append(value['delta']['day'])
          delta_week.append(value['delta']['week'])
          delta_month.append(value['delta']['month'])
          delta_quarter.append(value['delta']['quarter'])
          delta_year.append(value['delta']['year'])      

          # Getting current Date & Time
          timestamp, current_time, current_day, current_month_name, current_month, current_year, current_date_updated, current_hour = dt.current_date_time()           

          combined_data = pd.DataFrame(
                    { 'Time' : current_time, 
                    'Date': current_date_updated,
                    'Name': name,
                    'Rank' : rank,
                    'Age': age,
                    'Exchanges': exchanges,
                    'Markets': markets,
                    'Pairs' : pairs,
                    'All_Time_High' : alltimehigh,
                    'Circulating_Supply' : circulation,
                    'Total_Supply' : totalsupply,
                    'Max_Supply' : maxsupply,
                    'Code' : code,
                    'Rate' : rate,
                    'Volume' : volume,
                    'Cap' : cap,
                    # 'Liquidity' : liquidity,
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
          combined_data['Rank'] = combined_data['Rank'].astype('int')
          combined_data['Age'] = combined_data['Age'].astype('int')
          combined_data['Exchanges'] = combined_data['Exchanges'].astype('int')
          combined_data['Markets'] = combined_data['Markets'].astype('int')
          combined_data['Pairs'] = combined_data['Pairs'].astype('int')
          combined_data['All_Time_High'] = combined_data['All_Time_High'].astype('float')
          combined_data['Circulating_Supply'] = combined_data['Circulating_Supply'].astype('float')
          combined_data['Total_Supply'] = combined_data['Total_Supply'].astype('float')
          combined_data['Max_Supply'] = combined_data['Max_Supply'].astype('float')
          combined_data['Code'] = combined_data['Code'].astype('string')
          combined_data['Rate'] = combined_data['Rate'].astype('float')
          combined_data['Volume'] = combined_data['Volume'].astype('float')
          combined_data['Cap'] = combined_data['Cap'].astype('float')
          # combined_data['Liquidity'] = combined_data['Liquidity'].astype('int64')
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
        #   coin_name = combined_data[2]
          crypto_name_len = len(name)
          crypto_name = name[crypto_name_len -1]
          crypto_name = crypto_name.upper()
          file_name = f"{crypto_name}_{timestamp}.csv"
        #   print(file_name)

        
          with open('D:/Projects/Crypto/Data/FileName.py', 'w') as file:
              file.write(f"file_name = '{file_name}'\n")
          row_csv = combined_data.to_csv(index = False)

          # Establishing S3 connection
          s3_client = cc.get_connection()
          location = f"{crypto_name}/" + file_name
          s3_client.put_object(Bucket=va.bucket_name, Key=location, Body=row_csv)

          ue.update_excel(combined_data, name[crypto_name_len -1])

          # Loading data on DataBase
          for row in combined_data.itertuples():
        #   Sending data to MySQL Server
            lm.load_mysql(row, crypto_name)
              # Sending data to MsSQL Server
            ldb.load_mssql(row, name[crypto_name_len -1])
          print(combined_data)

if __name__ == '__main__':
   app.main()
        