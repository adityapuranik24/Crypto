import pyodbc



# def mssql(row):
def db_con():
    # Establishing connection
    curser = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                    "Server=ASUS\SQLEXPRESS;"
                    "Database=CRYPTO;"
                    "Trusted_Connection=yes;",
                    autocommit= True)
    return curser




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










