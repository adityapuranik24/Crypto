import streamlit as st
import sys
import pandas as pd
import datetime
sys.path.append('D:/Projects/Crypto/Scripts/S3')
sys.path.append('D:/Projects/Crypto/Scripts/Calculations')
sys.path.append('D:/Projects/Crypto/Scripts/Excel')
import Getting_Data_Excel as ex 
import Delta_Time as dt
import Getting_Data_S3 as s3

sys.path.append('D:/Projects/Crypto/Data')
import Variables as va

df = pd.read_csv(va.file_path)


current_time = datetime.datetime.now()
st.set_page_config(layout="wide")

def main():
    col1, col2 = st.columns([1, 30])
    with col1:
        st.image("https://cryptologos.cc/logos/bitcoin-btc-logo.png", width=50)
    with col2:
        st.title("Bitcoin")

    with st.container():
        # Define columns within the container
        col1, col2, col3, col4= st.columns([2.5,2.5,2.5,2.5])

        with col1:
            bitcoin_price = round(s3.get_data('Rate'), 2)
            st.metric("BITCOIN PRICE", f'${bitcoin_price}')

        with col2:
            market_cap = s3.get_data('Cap')
            market_cap_trillion = round((market_cap/1000000000000), 3)
            st.metric("MARKET CAP", f'{market_cap_trillion}T')    

        with col3:
            volume = s3.get_data('Volume')
            volume_billion = round((volume/1000000000),3)
            st.metric("VOLUME", f'{volume_billion}B')
        
        with col4:
            all_time_high = round(s3.get_data('All Time High'), 2)
            st.metric("VOLUME", f'${all_time_high}')
        
    with st.container():
        # Define columns within the container
        col1, col2, col3, col4= st.columns([2.5,2.5,2.5,2.5])

        with col1:
            cir_supply = round(s3.get_data('Circulating Supply'), 3)
            cir_supply_million = round((cir_supply/1000000), 3)
            st.metric("CIRCULATING SUPPLY", f'${cir_supply_million}M')

        with col2:
            total_supply = round(s3.get_data('Total Supply'), 3)
            total_supply_million = round((total_supply/1000000), 3)
            st.metric("TOTAL SUPPLY", f'${total_supply_million}M')   

        with col3:
            max_supply = round(s3.get_data('Max Supply'), 3)
            max_supply_million = round((max_supply/1000000), 3)
            st.metric("MAX SUPPLY", f'${max_supply_million}M')
        
        with col4:
            liquidity = s3.get_data('Liquidity')
            liquidity_billion = round((liquidity/1000000000), 3)
            st.metric("LIQUIDITY", f'${liquidity_billion}B') 

    with st.container():
        # Define columns within the container
        col1, col2, col3, col4= st.columns([2.5,2.5,2.5,2.5])

        with col1:
            hour_change = dt.rate_of_change('Delta Hour Change')
            st.metric("1H USD", f'{hour_change}%')

        with col2:
            day_change = dt.rate_of_change('Delta Day Change')
            st.metric("24H USD", f'{day_change}%')  

        with col3:
            week_change = dt.rate_of_change('Delta Week Change')
            st.metric("7D USD", f'{week_change}%')
        
        with col4:
            month_change = dt.rate_of_change('Delta Month Change')
            st.metric("30D USD", f'{month_change}%')

    st.markdown("""---""")
    st.write('Bitcoin Price Chart')
    st.line_chart(df, x= 'Volume', y = 'Rate', color="#FF0000")
    st.experimental_rerun()

if __name__ == "__main__":
    main()