


def create_table(cursor, exchange_name):
    cursor.execute(f'''
    CREATE TABLE `{exchange_name}` (
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
