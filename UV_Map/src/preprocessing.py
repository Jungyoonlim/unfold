import os 
import requests
from bs4 import BeautifulSoup
import time
import random

base_url = "https://archive.org/details/thingiverse"

response = requests.get(base_url)

soup = BeautifulSoup(response.text, 'html.parser')

links = soup.find_all('a')

# filter the links to get only those that point to ZIP files
zip_links = [link['href'] for link in links if link['href'].endswith('.zip')]

# download the first 500 zip files
for zip_link in zip_links[:500]:
    # The zip_link might be a relative URL, so we use urljoin to make it an absolute URL
    full_url = requests.compat.urljoin(base_url, zip_link)

    # Download the ZIP file
    zip_data = requests.get(full_url).content

    # Save it to disk
    with open(os.path.join('path_to_save_folder', os.path.basename(zip_link)), 'wb') as f:
        f.write(zip_data)

    # Delay to avoid overloading the server
    time.sleep(random.uniform(1, 3))