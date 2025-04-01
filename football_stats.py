import requests
from bs4 import BeautifulSoup

# URL of the CBS NFL Stats webpage for touchdowns
url = "https://www.cbssports.com/nfl/stats/leaders/live/touchdowns/regular/"

try:
  
    response = requests.get(url)
    response.raise_for_status() 

    
    soup = BeautifulSoup(response.content, 'html.parser')

   
    table = soup.find('table')

    if table:
        
        rows = table.find_all('tr')[1:21]  
        if len(rows) == 0:
            print("No player data found!")
        else:
            print(f"{'Player':<25} {'Position':<10} {'Team':<10} {'Touchdowns':<5}")
            print("=" * 60)

            
            for row in rows:
                cols = row.find_all('td')
                
                
                if len(cols) >= 4:
                    player = cols[0].text.strip()
                    position = cols[1].text.strip()
                    team = cols[2].text.strip()
                    touchdowns = cols[3].text.strip()
                    print(f"{player:<25} {position:<10} {team:<10} {touchdowns:<5}")
                else:
                    print("Warning: Row data is incomplete or not in expected format")
    else:
        print("Error: Stats table not found on the page")

except requests.RequestException as e:
    print(f"Error fetching data: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
