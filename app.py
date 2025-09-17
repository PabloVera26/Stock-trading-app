import requests
import dotenv
import os
import csv

dotenv.load_dotenv()
LIMIT = 100

POLYGON_APY_KEY = os.getenv("POLYGON_APY_KEY")

url = f"https://api.polygon.io/v3/reference/tickers?market=stocks&active=true&order=asc&limit={LIMIT}&sort=ticker&apiKey={POLYGON_APY_KEY}"

response = requests.get(url)
tickers = response.json()

print(tickers)

tickers_list = []
for ticker in tickers["results"]:
    tickers_list.append(ticker)

print(len(tickers_list))

csv_headers = [
    'ticker', 'name', 'market', 'locale', 'primary_exchange', 
    'type', 'active', 'currency_name', 'cik', 'composite_figi', 
    'last_updated_utc'
]

csv_filename = 'tickers.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_headers)
    writer.writeheader()
    
    for ticker_data in tickers_list:
        row = {}
        for header in csv_headers:
            row[header] = ticker_data.get(header, '')
        writer.writerow(row)

print(f"Tickers data saved to {csv_filename}")

example_structure = {
    'ticker': 'ACHR.WS', 
    'name': 'Archer Aviation Inc. Redeemable Warrants, each whole warrant exercisable for one Class A common stock at an exercise price of $11.50', 
    'market': 'stocks', 
    'locale': 'us', 
    'primary_exchange': 'XNYS', 
    'type': 'WARRANT', 
    'active': True, 
    'currency_name': 'usd', 
    'cik': '0001824502', 
    'composite_figi': 'BBG00YGCV1N9', 
    'last_updated_utc': '2025-09-16T06:05:51.696609632Z'
}