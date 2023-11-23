import requests
import streamlit as st
import pandas as pd

def get_crypto_price(coin_id):
    base_url = 'https://api.coingecko.com/api/v3'
    url = f"{base_url}/simple/price?ids={coin_id}&vs_currencies=usd"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data[coin_id]['usd']
    else:
        return None

# Your existing code for crypto holdings
crypto_holdings = {
    #'Bitcoin': {'amount': .5, 'purchase_price': 39000, 'purchase_date': '2022-01-01'},
    'Ethereum': {'amount': 0.0113886, 'purchase_price': 1790, 'purchase_date': '2022-01-01'},
    'Polygon': {'amount':46.69, 'purchase_price': 0.648, 'purchase_date': '2023-06-12'}
    # Add more cryptocurrencies and their amounts here
}

st.title('Crypto Holdings PNL Dashboard')

overall_invested = 0
overall_current_value = 0

st.write("## Individual Crypto Details")

for crypto, details in crypto_holdings.items():
    st.write(f"### {crypto}")
    st.write(f"Amount: {details['amount']}")
    st.write(f"Purchase Price: ${details['purchase_price']}")

    # Get current price
    current_price = get_crypto_price(crypto.lower())
    if current_price:
        current_price = float(current_price)
        current_value = details['amount'] * current_price
        overall_current_value += current_value

        st.write(f"Current Price: ${current_price}")
        st.write(f"Net PnL: ${current_value - (details['amount'] * details['purchase_price'])}")
    else:
        st.write("Failed to fetch current price for", crypto)

    overall_invested += details['amount'] * details['purchase_price']
    st.write("---")

# Show overall portfolio details
overall_pnl = overall_current_value - overall_invested

st.write("## Overall Portfolio Details")
st.write(f"Total Invested Amount: ${overall_invested}")
st.write(f"Current Portfolio Value: ${overall_current_value}")
st.write(f"Overall Net PnL: ${overall_pnl}")
