from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager  # To automatically install ChromeDriver
import time

# URL to scrape
url = "https://investor.apple.com/stock-price/default.aspx"

# Set up options for headless mode (optional)
options = Options()
options.headless = False  # Change to True to run the browser in the background

# Set up the WebDriver (using Chrome in this example)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Open the page
    driver.get(url)

    # Wait for the page to load (you can adjust this if needed)
    time.sleep(5)  # Sleep for 5 seconds, or use WebDriverWait for better synchronization

    # Find the stock price element (you might need to inspect the page to get the right CSS selector)
    stock_price_section = driver.find_element(By.CSS_SELECTOR, '.investor-relations-stock-price')

    # Extract the stock price and date
    price = stock_price_section.find_element(By.CSS_SELECTOR, '.quote-price')
    date = stock_price_section.find_element(By.CSS_SELECTOR, '.quote-date')

    # Print the extracted data
    print(f"Apple Stock Price:


