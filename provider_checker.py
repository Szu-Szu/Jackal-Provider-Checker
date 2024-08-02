import requests
from bs4 import BeautifulSoup

# List of URLs to check
websites = [
#   "add providers here",
    
]

# searching
search_text = "1.0.0"

def check_website(url, search_text):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        content = response.text
        
        
        soup = BeautifulSoup(content, 'html.parser')
        
        
        if search_text in soup.get_text():
            return True
        else:
            return False
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return False

# Loopty loop through the URLs
for site in websites:
    if check_website(site, search_text):
        print(f"Site {site} can receive grants.")
    else:
        print(f"Site {site} cannot receive grants.")
