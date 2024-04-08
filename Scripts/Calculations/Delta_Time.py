import sys
sys.path.append('D:/Projects/Crypto/Scripts/S3')
import Getting_Data_S3 as s3




def rate_of_change(time):

    delta_time = s3.get_data(time)
    current_price = s3.get_data('Rate')

    if delta_time >1.000:
        rate_of_change =round( delta_time - 1.000, 5)
        absolute_change = current_price * rate_of_change
        per_change = round((absolute_change/current_price) * 100, 2)
        return(f'+{per_change}')

    else:
        rate_of_change = 1.000 - delta_time
        absolute_change = current_price * rate_of_change
        per_change = round((absolute_change/current_price) * 100, 2)
        return(f'-{per_change}')