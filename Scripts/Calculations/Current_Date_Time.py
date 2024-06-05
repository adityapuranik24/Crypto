import sys
import datetime
from datetime import datetime



def current_date_time():
    # Getting current time 
    current_time = datetime.now().time()
    current_time = current_time.strftime("%H:%M:%S")

    # getting current date
    current_date = datetime.now()
    current_day = current_date.day
    current_month_name = current_date.strftime("%B")
    current_month = current_date.month
    current_year = current_date.year
    current_date_updated = current_date.strftime("%d %B %Y").upper()
    return current_time, current_day, current_month_name, current_month, current_year, current_date_updated



# a = current_date_time()
# print(a)