import pandas as pd
import pyodbc


conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                    "Server=ASUS\SQLEXPRESS;"
                    "Database=CRYPTO;"
                    "Trusted_Connection=yes;",
                    autocommit= True)


# conn.execute(''' CREATE TABLE BITCOIN (
#     Time VARCHAR(30),
#     Date DATE,
#     Name VARCHAR(20),
#     Age INT,
#     Exchanges INT,
#     Markets INT,
#     All_Time_High FLOAT,
#     Circulating_Supply BIGINT,
#     Total_Supply BIGINT,
#     Max_Supply BIGINT,
#     Rate FLOAT,
#     Volume BIGINT,
#     Cap BIGINT,
#     Liquidity BIGINT,
#     Delta_Hour_Change FLOAT,
#     Delta_Day_Change FLOAT,
#     Delta_Week_Change FLOAT,
#     Delta_Month_Change FLOAT,
#     Delta_Quarter_Change FLOAT,
#     Delta_Year_Change FLOAT,
#     Day INT,
#     Month_Number INT,
#     Month_Name VARCHAR(20),
#     Year INT
# );''')

# country_codes = pd.read_csv("D:\Projects\Crypto\Cleaned Data\sample_data.csv")
# country_codes
# for row in country_codes.itertuples():
#     conn.execute('''
#                     INSERT INTO BITCOIN (
#                   Time, Date, Name, Age, Exchanges, Markets, All_Time_High, Circulating_Supply, Total_Supply,
#                   Max_Supply, Rate, Volume, Cap, Liquidity, Delta_Hour_Change, Delta_Day_Change,
#                   Delta_Week_Change, Delta_Month_Change, Delta_Quarter_Change, Delta_Year_Change, Day, Month_Number, 
#                   Month_Name, Year ) 
#                   VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
#                     ''',
#                     (row.Time, 
#                     row.Date,
#                     row.Name, 
#                     row.Age,
#                     row.Exchanges,
#                     row.Markets, 
#                     row.All_Time_High,
#                     row.Circulating_Supply,
#                     row.Total_Supply, 
#                     row.Max_Supply,
#                     row.Rate,
#                     row.Volume, 
#                     row.Cap,
#                     row.Liquidity,
#                     row.Delta_Hour_Change, 
#                     row.Delta_Day_Change,
#                     row.Delta_Week_Change,
#                     row.Delta_Month_Change, 
#                     row.Delta_Quarter_Change,
#                     row.Delta_Year_Change,
#                     row.Day,
#                     row.Month_Number,
#                     row.Month_Name,
#                     row.Year)
                    
#                     )
# conn.commit()









