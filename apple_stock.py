from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager  # To automatically install ChromeDriver
import time

# URL to scrape
url = "https://finance.yahoo.com/quote/AAPL/history?p=AAPL"

# Set up options for headless mode (optional)
options = Options()
options.headless = False  # Change to True to run the browser in the background

# Set up the WebDriver (using Chrome in this example)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Open the page
    driver.get(url)

    # Wait for the page to load (adjust the wait time as needed)
    time.sleep(5)  # Sleep for 5 seconds, or use WebDriverWait for better synchronization

    # Locate the table containing historical data (ensure you inspect the correct table)
    rows = driver.find_elements(By.CSS_SELECTOR, 'table[data-test="historical-prices"] tbody tr')

    # Iterate through the rows and extract the date and closing price
    for row in rows:
        try:
            # Extract the date and closing price from each row
            date = row.find_element(By.CSS_SELECTOR, 'td[data-test="date"] span').text
            close_price = row.find_element(By.CSS_SELECTOR, 'td[data-test="close"] span').text
            print(f"Date: {date}, Close Price: {close_price}")
        except Exception as e:
            print(f"Error extracting data from row: {e}")
    
except Exception as e:
    print(f"Error fetching data: {e}")

finally:
    # Close the driver
    driver.quit()


