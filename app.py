import requests
import dotenv
import os

dotenv.load_dotenv()

POLYGON_APY_KEY = os.getenv("POLYGON_APY_KEY")
LIMIT = 100

url = f"https://api.polygon.io/v3/reference/tickers?market=stocks&active=true&order=asc&limit={LIMIT}&sort=ticker&apiKey={POLYGON_APY_KEY}"

response = requests.get(url)
tickers = response.json()

print(tickers)

tickers_list = []
for ticker in tickers["results"]:
    tickers_list.append(ticker["ticker"])

print(len(tickers_list))