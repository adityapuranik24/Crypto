import pymysql



def db_connect():
    db = pymysql.connect(host="db-crypto.c9wekkiy8fip.us-east-2.rds.amazonaws.com", 
                        user = "admin", password="Addi8881212")
    cursor = db.cursor()
    return cursor, db


a,b = db_connect()
a.execute('''USE CRYPTO''')
print(a.execute('''SELECT * FROM BITCOIN;'''))
# print(a.execute(''' CREATE TABLE BITCOIN (
#     Time VARCHAR(20),
#     Name VARCHAR(20),
#     Age INT,
#     Exchanges VARCHAR(20),
#     Markets VARCHAR(20),
#     All_Time_High FLOAT,
#     Circulating_Supply BIGINT,
#     Total_Supply BIGINT,
#     Max_Supply BIGINT,
#     Rate FLOAT,
#     Volume BIGINT,
#     Cap BIGINT,
#     Liquidity FLOAT,
#     Delta_Hour_Change FLOAT,
#     Delta_Day_Change FLOAT,
#     Delta_Week_Change FLOAT,
#     Delta_Month_Change FLOAT,
#     Delta_Year_Change FLOAT
# );'''))

rows = a.fetchall()

# Print each row
for row in rows:
    print(row)

