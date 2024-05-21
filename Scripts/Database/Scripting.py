import sys
import pandas as pd
sys.path.append('D:/Projects/Crypto/Database')
import MySQL_Connection as db_conn


cursor = db_conn.db_connect()
cursor.execute("CREATE DATABASE IF NOT EXISTS CRYPTO")
# Select the database
cursor.execute("USE CRYPTO")

# # Create a new table
# cursor.execute( """
#     CREATE TABLE IF NOT EXISTS BITCOIN (
#         Name VARCHAR(20),
#         Age INT,
#         Exchanges INT,
#         Markets INT,
#         All_Time_High FLOAT,
#         Circulating_Supply BIGINT,
#         Total_Supply BIGINT,
#         Max_Supply BIGINT,
#         Rate FLOAT,
#         Volume BIGINT,
#         Cap BIGINT,
#         Liquidity BIGINT,
#         Delta_Hour_Change FLOAT,
#         Delta_Day_Change FLOAT,
#         Delta_Week_Change FLOAT,
#         Delta_Month_Change FLOAT,
#         Delta_Year_Change FLOAT
#     );
#     """)

# print(cursor.execute("SELECT * FROM BITCOIN;"))

data = {
    "Name": ["Bitcoin"],
    "Age": [3995],
    "Exchanges": [188],
    "Markets": [3081],
    "All_Time_High": [73781.24185982272],
    "Circulating_Supply": [19676437],
    "Total_Supply": [19676437],
    "Max_Supply": [21000000],
    "Rate": [69450.12130532124],
    "Volume": [16752785068],
    "Cap": [1366530936506],
    "Liquidity": [1322160042],
    "Delta_Hour_Change": [1.0012],
    "Delta_Day_Change": [1.0014],
    "Delta_Week_Change": [0.9823],
    "Delta_Month_Change": [1.0159],
    "Delta_Year_Change": [2.4583]
}
df = pd.DataFrame(data)

insert_query = """
        INSERT INTO BITCOIN (
            Name, Age, Exchanges, Markets, All_Time_High, Circulating_Supply, Total_Supply,
            Max_Supply, Rate, Volume, Cap, Liquidity, Delta_Hour_Change, Delta_Day_Change,
            Delta_Week_Change, Delta_Month_Change, Delta_Year_Change
        ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);
        """


cursor.execute(insert_query, df)