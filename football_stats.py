# football_stats.py
"""
Script to scrape top 20 touchdown leaders from CBS NFL Stats
URL: https://www.cbssports.com/nfl/stats/
"""

import requests
from bs4 import BeautifulSoup

url = "https://www.cbssports.com/nfl/stats/"

try:
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

   
    table = soup.find('table')
    rows = table.find_all('tr')[1:21]  

    print(f"{'Rank':<5}{'Player':<25}{'Position':<10}{'Team':<10}{'Touchdowns':<10}")

    for index, row in enumerate(rows, start=1):
        cols = row.find_all('td')
        player = cols[0].get_text(strip=True)
        position = cols[1].get_text(strip=True)
        team = cols[2].get_text(strip=True)
        touchdowns = cols[6].get_text(strip=True)  

        print(f"{index:<5}{player:<25}{position:<10}{team:<10}{touchdowns:<10}")

except Exception as e:
    print("Error fetching data:", e)
