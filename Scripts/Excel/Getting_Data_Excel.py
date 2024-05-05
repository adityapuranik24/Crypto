import pandas as pd
import sys
sys.path.append('D:/Projects/Crypto/Data')
import Variables as va


def getting_price():
    df = pd.read_csv(va.file_path)
    # price = round(df['Rate'], 2)
    # print(type(df))
    return df


# a = getting_price()
# print(a)