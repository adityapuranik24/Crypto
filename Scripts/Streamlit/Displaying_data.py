import streamlit as st
import sys
sys.path.append('D:/Projects/Crypto/Scripts/S3')
import Getting_Data_S3 as s3



def main():
    st.title("Bitcoin Tracker")
    st.image("D:/Projects/Crypto/Data/Bitcoin-Logo.png", width=50)

    col1, col2, col3 = st.columns(3)

    with col1:
        bitcoin_price = s3.get_data('Rate')
        st.metric("Bitcoin Price", bitcoin_price)

    with col2:
        market_cap = s3.get_data('Cap')
        st.metric("Market Cap", market_cap)    

    with col3:
        Volume = s3.get_data('Volume')
        st.metric("Volume", Volume)

    st.experimental_rerun()

if __name__ == "__main__":
    main()