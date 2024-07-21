


def create_table(curser, exchange_name):
    curser.execute(f'''
CREATE TABLE IF NOT EXSIST {exchange_name} (
    Time VARCHAR(30),
    Date DATE,
    Name VARCHAR(30),
    Coin_Name VARCHAR(30),
    Code VARCHAR(10),
    Volume FLOAT,
    Bid_Total FLOAT,
    Ask_Total FLOAT,
    Depth FLOAT,
    Hour INT,
    Day INT,
    Month_Number INT,
    Month_Name VARCHAR(30),
    Year INT
);
''')
    
    