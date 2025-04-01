# apple_stock.py
"""
Script to scrape Apple's historical closing prices from Yahoo Finance
URL: https://finance.yahoo.com/quote/AAPL/history?p=AAPL
"""

import requests
from bs4 import BeautifulSoup

url = "https://finance.yahoo.com/quote/AAPL/history?p=AAPL"

try:
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')


    table = soup.find('table')
    rows = table.find_all('tr')

    print(f"{'Date':<20}{'Close Price':<15}")

    for row in rows[1:]: 
        cols = row.find_all('td')
        if len(cols) >= 6:
            date = cols[0].get_text(strip=True)
            close_price = cols[4].get_text(strip=True)  
            print(f"{date:<20}{close_price:<15}")

except Exception as e:
    print("Error fetching data:", e)
