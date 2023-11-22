import requests


base_url = 'https://api.coingecko.com/api/v3'

# Example list of cryptos you hold and their amounts
crypto_holdings = {
    'Bitcoin': {'amount': 1.5, 'purchase_price': 50000},
    'Ethereum': {'amount': 0.0113886, 'purchase_price': 1790},
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

with open('crypto_holdings.txt', 'w') as file:
    for crypto, details in crypto_holdings.items():
        price = get_crypto_price(crypto.lower())
        if price:
            current_price = float(price)
            pnl = calculate_profit_loss(details['amount'], details['purchase_price'], current_price)
            file.write(f"Crypto: {crypto}\n")
            file.write(f"Amount: {details['amount']}\n")
            file.write(f"Purchase Price: ${details['purchase_price']}\n")
            file.write(f"Current Price: ${current_price}\n")
            file.write(f"Net PnL: ${pnl}\n")
            file.write("=====================\n")

print("Data written to crypto_holdings.txt")
