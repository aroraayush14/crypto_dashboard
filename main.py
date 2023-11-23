import requests
import streamlit as st
import pandas as pd

base_url = 'https://api.coingecko.com/api/v3'

# Example list of cryptos you hold and their amounts
crypto_holdings = {
    'Bitcoin': {'amount': 1.5, 'purchase_price': 50000, 'purchase_date': '2022-01-01'},
    'Ethereum': {'amount': 0.0113886, 'purchase_price': 1790, 'purchase_date': '2022-01-01'},
    # Add more cryptocurrencies and their amounts here
}

def get_crypto_price(coin_id):
    url = f"{base_url}/simple/price?ids={coin_id}&vs_currencies=usd"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data[coin_id]['usd']
    else:
        return None

def calculate_profit_loss(amount, purchase_price, current_price):
    invested_amount = amount * purchase_price
    current_value = amount * current_price
    pnl = current_value - invested_amount
    return pnl

st.title('Crypto Holdings PNL Dashboard')

pnl_data = {'Crypto': [], 'PNL': []}

for crypto, details in crypto_holdings.items():
    price = get_crypto_price(crypto.lower())
    if price:
        current_price = float(price)
        pnl = calculate_profit_loss(details['amount'], details['purchase_price'], current_price)
        pnl_data['Crypto'].append(crypto)
        pnl_data['PNL'].append(pnl)
        st.write(f"### {crypto}")
        st.write(f"Amount: {details['amount']}")
        st.write(f"Purchase Price: ${details['purchase_price']}")
        st.write(f"Current Price: ${current_price}")
        st.write(f"Net PnL: ${pnl}")
        st.write("---")

# Dummy historical PNL data (Replace this with actual historical data)
historical_data = {
    'Date': pd.date_range('2022-01-01', periods=10),
    'Bitcoin': [37000, 37600, 150, 130, 140, 160, 180, 170, 190, 200],
    'Ethereum': [50, 60, 70, 80, 90, 100, 110, 120, 130, 140]
}

df = pd.DataFrame(historical_data)
df = df.set_index('Date')

st.write("## Historical PNL Trends")

# Modify DataFrame based on purchase date for each cryptocurrency
for crypto, details in crypto_holdings.items():
    purchase_date = pd.to_datetime(details['purchase_date'])
    filtered_df = df[df.index >= purchase_date]
    st.line_chart(filtered_df[crypto])
