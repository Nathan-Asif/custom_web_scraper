# Title : ITSN Custom Web Scraper
# Description : Custom Web Scraper made with ZenRows web scraping service to scrap website pages/data that are containing CloudFlare AntiBot Restrictions.
# Contact : itsnathan.net@gmail.com

import os
from bs4 import BeautifulSoup
from zenrows import ZenRowsClient

def sanitize_filename(filename):
    """Sanitize the filename by removing characters not allowed in filenames."""
    illegal_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    for char in illegal_chars:
        filename = filename.replace(char, '')
    return filename

# Create a folder named 'scrapes' if it doesn't exist
if not os.path.exists('scrapes'):
    os.makedirs('scrapes')

# Initialize ZenRowsClient
client = ZenRowsClient("YOUR_API_ZENROW_KEY")
url = "https://worldwidetopsite.link/website-list-1015/"
# SignUp on Zenrows: https://zenrows.com/ to obtain your free API Key.

# Get response
response = client.get(url)

# Parse HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Get the title of the webpage and sanitize it
title = sanitize_filename(soup.title.string.strip())

# Create a new HTML file with the sanitized title of the webpage as the filename
filename = os.path.join('scrapes', f"{title}.html")

# Write the HTML content to the file
with open(filename, 'w', encoding='utf-8') as file:
    file.write(response.text)

print(f"HTML file '{filename}' has been created with the scraped content.")