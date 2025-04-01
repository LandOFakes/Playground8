import requests
from bs4 import BeautifulSoup

# URL of Apple's stock price
url = "https://investor.apple.com/stock-price/default.aspx"

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

    # Find the stock price in the page
    stock_price_section = soup.find('div', class_='investor-relations-stock-price')

    if stock_price_section:
        # Extract the current stock price and date
        price = stock_price_section.find('span', class_='quote-price')
        date = stock_price_section.find('span', class_='quote-date')

        if price and date:
            print(f"Apple Stock Price: {price.text.strip()}")
            print(f"Last Updated: {date.text.strip()}")
        else:
            print("Error: Could not find stock price data on the page")
    else:
        print("Error: Could not find the stock price section on the page")

except requests.RequestException as e:
    print(f"Error fetching data: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
