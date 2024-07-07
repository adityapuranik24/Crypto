import pyodbc
import pandas as pd


# def mssql(row):
def db_con():
    # Establishing connection
    curser = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                    "Server=ASUS\SQLEXPRESS;"
                    "Database=CRYPTO;"
                    "Trusted_Connection=yes;",
                    autocommit= True)
    return curser

# a = db_con()


# a.execute(''' CREATE TABLE XRP (
#     Time VARCHAR(30),
#     Date DATE,
#     Name VARCHAR(30),
#     Rank INT,
#     Age INT,
#     Exchanges INT,
#     Markets INT,
#     Pairs INT,
#     All_Time_High FLOAT,
#     Circulating_Supply FLOAT,
#     Total_Supply FLOAT,
#     Max_Supply FLOAT,
#     Code VARCHAR(10),
#     Rate FLOAT,
#     Volume FLOAT,
#     Cap FLOAT,
#     Delta_Hour_Change FLOAT,
#     Delta_Day_Change FLOAT,
#     Delta_Week_Change FLOAT,
#     Delta_Month_Change FLOAT,
#     Delta_Quarter_Change FLOAT,
#     Delta_Year_Change FLOAT,
#     Hour INT,
#     Day INT,
#     Month_Number INT,
#     Month_Name VARCHAR(50),
#     Year INT
# );''')









