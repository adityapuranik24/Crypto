import sys
sys.path.extend([
    'D:/Projects/Crypto/Database'])
import MS_SQL_Connection as db_conn


def load_mssql(row, name):
    curser = db_conn.db_con()

    # Inserting Data
    curser.execute(f'''
                    INSERT INTO [{name}] (
                    Time, Date, Name, Rank, Age, Exchanges, Markets, Pairs, All_Time_High, Circulating_Supply, Total_Supply,
                    Max_Supply, Code, Rate, Volume, Cap, Delta_Hour_Change, Delta_Day_Change,
                    Delta_Week_Change, Delta_Month_Change, Delta_Quarter_Change, Delta_Year_Change, Hour, Day, Month_Number, 
                    Month_Name, Year ) 
                  VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                    ''',
                    (row.Time, 
                        row.Date,
                        row.Name,
                        row.Rank, 
                        row.Age,
                        row.Exchanges,
                        row.Markets,
                        row.Pairs, 
                        row.All_Time_High,
                        row.Circulating_Supply,
                        row.Total_Supply, 
                        row.Max_Supply,
                        row.Code,
                        row.Rate,
                        row.Volume, 
                        row.Cap,
                        row.Delta_Hour_Change, 
                        row.Delta_Day_Change,
                        row.Delta_Week_Change,
                        row.Delta_Month_Change, 
                        row.Delta_Quarter_Change,
                        row.Delta_Year_Change,
                        row.Hour,
                        row.Day,
                        row.Month_Number,
                        row.Month_Name,
                        row.Year)
                    
                    )
    curser.commit()
