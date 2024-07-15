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
import Loading_MySQL as lm
import Loading_MsSQL as ldb
import S3_Client_Connection as cc
import Updating_Excel as ue
import Variables as va



app=faust.App('demo-streaming',broker='kafka://18.217.211.255:9092')
input_topic = app.topic('crypto', value_serializer='json')
@app.agent(input_topic)
async def processor(stream):    
    name = []
    centralized = []
    usCompliant = []
    code = []
    markets = []
    volume = []
    bidTotal = []
    askTotal = []
    depth = []
    visitors = []
    volumePerVisitor = []

    
    async for message in stream:
        print(message)
        value = []
        length = len(message)
        for i in range (0,length):
            value = message[i]
            rem_list = ['png64', 'png128', 'webp64','webp128']
            for key in rem_list:
                if key in value:
                    del value[key]
            # print(value)

        name.append(value['name'])
        centralized.append(value['rank'])
        usCompliant.append(value['age'])
        code.append(value['exchanges'])
        markets.append(value['markets'])
        volume.append(value['pairs'])
        bidTotal.append(value['allTimeHighUSD'])
        askTotal.append(value['circulatingSupply'])
        depth.append(value['totalSupply'])
        visitors.append(value['maxSupply'])
        volumePerVisitor.append(value['code'])  

          # Getting current Date & Time
        timestamp, current_time, current_day, current_month_name, current_month, current_year, current_date_updated, current_hour = dt.current_date_time()           

        combined_data = pd.DataFrame(
                  { 'Time' : current_time, 
                  'Date': current_date_updated,
                  'Name': name,
                  'Centralized' : centralized,
                  'US_Compliant': usCompliant,
                  'Code': code,
                  'Markets': markets,
                  'Volume' : volume,
                  'Bid_Total' : bidTotal,
                  'Ask_Total' : askTotal,
                  'Depth' : depth,
                  'Visitors' : visitors,
                  'Volume_PerVisitor' : volumePerVisitor,
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
        combined_data['Centralized'] = combined_data['Centralized'].astype('int')
        combined_data['US_Compliant'] = combined_data['US_Compliant'].astype('int')
        combined_data['Code'] = combined_data['Code'].astype('int')
        combined_data['Markets'] = combined_data['Markets'].astype('int')
        combined_data['Volume'] = combined_data['Volume'].astype('int')
        combined_data['Bid_Total'] = combined_data['Bid_Total'].astype('float')
        combined_data['Ask_Total'] = combined_data['Ask_Total'].astype('float')
        combined_data['Depth'] = combined_data['Depth'].astype('float')
        combined_data['Visitors'] = combined_data['Visitors'].astype('float')
        combined_data['Volume_PerVisitor'] = combined_data['Volume_PerVisitor'].astype('string')
        combined_data['Hour'] = combined_data['Hour'].astype('int') 
        combined_data['Day'] = combined_data['Day'].astype('int') 
        combined_data['Month_Number'] = combined_data['Month_Number'].astype('int')  
        combined_data['Month_Name'] = combined_data['Month_Name'].astype('string') 
        combined_data['Year'] = combined_data['Year'].astype('int')  

          # Creating a file for each entry with timestamp to save in S3 storge
          # current_time = datetime.datetime.now()
        #   coin_name = combined_data[2]
        exchange_name_len = len(name)
        exchange_name = name[exchange_name_len -1]
        exchange_name = exchange_name.upper()
        file_name = f"{exchange_name}_{timestamp}.csv"
        #   print(file_name)

        
        with open('D:/Projects/Crypto/Data/FileName.py', 'w') as file:
            file.write(f"exchange_name = '{file_name}'\n")
        row_csv = combined_data.to_csv(index = False)

          # Establishing S3 connection
        s3_client = cc.get_connection()
        location = f"{exchange_name}/" + file_name
        s3_client.put_object(Bucket=va.bucket_name, Key=location, Body=row_csv)

        ue.update_excel(combined_data, name[exchange_name_len -1])

          # Loading data on DataBase
        for row in combined_data.itertuples():
      #   Sending data to MySQL Server
          lm.load_mysql(row, crypto_name)
            # Sending data to MsSQL Server
          ldb.load_mssql(row, name[crypto_name_len -1])
        print(combined_data)

if __name__ == '__main__':
   app.main()
        