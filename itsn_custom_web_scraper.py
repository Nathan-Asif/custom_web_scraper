import os
import json
import logging
from bs4 import BeautifulSoup
from zenrows import ZenRowsClient

logging.basicConfig(level=logging.INFO)

def sanitize_filename(filename):
    """Sanitize the filename by removing characters not allowed in filenames."""
    illegal_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    for char in illegal_chars:
        filename = filename.replace(char, '')
    # Additional sanitization for Windows compatibility
    filename = filename.rstrip('.')  # Remove trailing dots
    filename = filename.strip()  # Remove leading/trailing whitespaces
    return filename

def initializeRequest(url):
    # Initialize ZenRowsClient
    client = ZenRowsClient("YOUR_API_KEY")
    # SignUp on Zenrows: https://zenrows.com/ to obtain your free API Key.

    try:
        # Get response
        params = {"js_render":"true"}
        response = client.get(url, params=params)
        print("Requesting Data...")

        data = response.text
        print(response.text)
        
        # Parse HTML content
        soup = BeautifulSoup(data, 'html.parser')

        # Get the title of the webpage and sanitize it
        title = sanitize_filename(soup.title.string.strip())

        # Create a new HTML file with the sanitized title of the webpage as the filename
        filename = os.path.join('scrapes', f"{title}.html")

        # Write the HTML content to the file
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(response.text)

        logging.info(f"HTML file '{filename}' has been created with the scraped content.")
    except Exception as e:
        logging.error(f"Failed to scrape URL: {url}. Error: {str(e)}")

# Counter for increment in url slug
slug_counter = 1251
number_of_pages = 1

# Loop to iterate over specified number of urls
for _ in range(number_of_pages):
    # Create a folder named 'scrapes' if it doesn't exist
    if not os.path.exists('scrapes'):
        os.makedirs('scrapes')
    url = f"https://worldwidetopsite.link/website-list-{slug_counter}/"
    logging.info(url)
    # Function to make request over target url to scrape the data
    initializeRequest(url)
    slug_counter += 1