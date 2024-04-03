import streamlit as st
import sys
sys.path.append('D:/Projects/Crypto/Scripts/Streamlit')
import Dashboard as db



def main():
    st.title('Bitcoin Live Price Tracker')

    # Fetching Bitcoin data
    bitcoin_price = db.get_data()

    # Displaying the data
    st.metric(label="Bitcoin Price", value=bitcoin_price)

    # Refresh button to update the price
    
    st.experimental_rerun()

if __name__ == "__main__":
    main()