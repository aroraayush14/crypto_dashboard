# Crypto Portfolio Profit/Loss Calculator

This Python script calculates the profit or loss of a cryptocurrency portfolio based on the current market prices fetched from the CoinGecko API. It generates a `crypto_holdings.txt` file containing a summary of each cryptocurrency's details, including the initial purchase price, current market price, and net profit or loss.

## Prerequisites

Before using this script, ensure you have the following installed:

- Python 3.9
- `requests` library (`pip install requests`)

## Setup

1. Clone or download this repository to your local machine.
2. Ensure you have Python installed.
3. Install the required `requests` library using pip: `pip install requests`.

## Usage

1. Open the `crypto_holdings.py` file.
2. Modify the `crypto_holdings` dictionary to include your cryptocurrencies and their respective amounts and purchase prices.
3. Run the script by executing: `python crypto_holdings.py`.
4. After execution, a file named `crypto_holdings.txt` will be generated containing the portfolio summary.

## Code Structure

- `base_url`: The base URL for accessing the CoinGecko API.
- `crypto_holdings`: Dictionary containing cryptocurrencies, their amounts, and purchase prices.
- `get_crypto_price(coin_id)`: Function to fetch the current price of a cryptocurrency using its ID from the CoinGecko API.
- `calculate_profit_loss(amount, purchase_price, current_price)`: Function to calculate the profit or loss for a specific cryptocurrency based on the provided details.
- The script iterates through the `crypto_holdings` dictionary, fetches current prices, and calculates profit/loss for each cryptocurrency, writing the details to `crypto_holdings.txt`.

## Important Note

- The script uses the CoinGecko API to fetch real-time prices. Ensure a stable internet connection to fetch accurate data.

Feel free to update the code to suit your needs or add more functionality.
