import requests
from bs4 import BeautifulSoup

# URL of the Wikipedia page
url = "https://en.wikipedia.org/wiki/List_of_NFL_annual_passing_touchdowns_leaders"

try:
    # Fetch the webpage content
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful

    # Parse the page content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Locate all tables with the class 'wikitable'
    tables = soup.find_all('table', {'class': 'wikitable'})

    # Check if tables are found
    if tables:
        # Use the first relevant table (the one with passing touchdowns)
        for table in tables:
            rows = table.find_all('tr')

            # Print the header
            print(f"{'Year':<6} {'Player':<25} {'Team':<20} {'TDs':<5}")
            print("=" * 60)

            # Iterate through each row, starting from the second row to skip the header
            for row in rows[1:]:
                cols = [col.get_text(strip=True) for col in row.find_all(['th', 'td'])]

                # Check if the row has at least 4 columns (year, player, team, touchdowns)
                if len(cols) >= 4:
                    year = cols[0]
                    player = cols[1]
                    team = cols[2]
                    touchdowns = cols[3]

                    # Print the formatted result
                    print(f"{year:<6} {player:<25} {team:<20} {touchdowns:<5}")
                else:
                    # Skip rows that don't contain player data
                    continue

    else:
        print("Error: Could not find the statistics table on the page")

except requests.RequestException as e:
    print(f"Error fetching data: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
