import pandas as pd
import sys
sys.path.append('D:/Projects/Crypto/Data')
import Variables as va

def update_excel(data, currency_name):
    data.to_csv(f"D:/Projects/Crypto-Develop/Crypto-Develop/Cleaned Data/{currency_name}.csv", mode='a', index=False, header=False)

