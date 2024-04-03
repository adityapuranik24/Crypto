import pandas as pd
import sys
sys.path.append('D:/Projects/Crypto/Data')
import Variables as va

def update_excel(data):
    data.to_csv(va.file_path, mode='a', index=False, header=False)

