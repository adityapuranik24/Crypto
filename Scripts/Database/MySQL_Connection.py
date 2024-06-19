import pymysql
import pandas as pd


def db_connect():
    db = pymysql.connect(host="db-crypto.c9wekkiy8fip.us-east-2.rds.amazonaws.com", 
                        user = "admin", password="Addi8881212")
    cursor = db.cursor()
    return cursor, db



# a.execute('''USE CRYPTO''')
# # print(a.execute('''SELECT * FROM BITCOIN;'''))
# print(a.execute(''' CREATE TABLE BITCOIN (
#     Time VARCHAR(30),
#     Date DATE,
#     Name VARCHAR(20),
#     Age INT,
#     Exchanges INT,
#     Markets INT,
#     All_Time_High FLOAT,
#     Circulating_Supply FLOAT, 
#     Total_Supply FLOAT, 
#     Max_Supply FLOAT, 
#     Rate FLOAT,
#     Volume FLOAT, 
#     Cap FLOAT, 
#     Liquidity FLOAT, 
#     Delta_Hour_Change FLOAT,
#     Delta_Day_Change FLOAT,
#     Delta_Week_Change FLOAT,
#     Delta_Month_Change FLOAT,
#     Delta_Quarter_Change FLOAT,
#     Delta_Year_Change FLOAT,
#     Hour INT,
#     Day INT,
#     Month_Number INT,
#     Month_Name VARCHAR(20),
#     Year INT
# );'''))





# rows = a.fetchall()

# # Print each row
# for row in rows:
#     print(row)

