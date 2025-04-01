import requests
from bs4 import BeautifulSoup
import time

# URL of the Apple stock historical data
url = "https://finance.yahoo.com/quote/AAPL/history?p=AAPL"

# Set up headers to make the request look like it's from a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

try:
    # Fetch the webpage content with headers
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Check if the request was successful

    # Parse the page content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the historical data table
    table = soup.find('table', {'data-test': 'historical-data-table'})

    if table:
        # Extract all rows from the table
        rows = table.find_all('tr')[1:]  # Skip the header row

        # Print the header
        print(f"{'Date':<12} {'Close Price':<15}")
        print("=" * 30)

        # Iterate through each row
        for row in rows:
            cols = row.find_all('td')

            # Ensure the row has the expected columns
            if len(cols) > 0:
                date = cols[0].text.strip()
                close_price = cols[4].text.strip()  # Close price is in the 5th column (index 4)

                # Print the formatted
