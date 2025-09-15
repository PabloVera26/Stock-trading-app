import requests
import dotenv
import os

dotenv.load_dotenv()

POLYGON_APY_KEY = os.getenv("POLYGON_APY_KEY")

def get_stock_data():
    url = f"https://api.polygon.io/v3/reference/tickers?market=stocks&active=true&order=asc&limit=100&sort=ticker&apiKey={POLYGON_APY_KEY}"
    response = requests.get(url)
    return response.json()

print(get_stock_data())