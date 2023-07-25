import requests
from bs4 import BeautifulSoup
import os
import random
import time

def get_free_model_urls():
    free_model_urls = []
    base_url = 'https://www.turbosquid.com/Search/3D-Models/free'
    try:
        response = requests.get(base_url)

        if response.status_code != 200:
            print(f"Failed to get models from URL {base_url}. Server responded with status code {response.status_code}.")
            return free_model_urls

        soup = BeautifulSoup(response.text, 'html.parser')
        all_models = soup.find_all('a')  # Get all 'a' tags

        for model in all_models:
            free_item = model.find('div', class_='free_item')  # Check if a 'div' with class 'free_item' exists
            if free_item and free_item.text.strip() == 'Free':  # Check if the text within the div is 'Free'
                free_model_urls.append(model['href'])

    except Exception as e:
        print(f"Error occurred while getting free model URLs: {e}")

    return free_model_urls

def check_uv_mapping(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find UV Mapped tag using its ID
        uv_mapped_tag = soup.find('span', {'id': 'FPSpec_uv_mapped'})

        if uv_mapped_tag is not None:
            print(f"UV Mapped tag found for URL: {url}")
            return True

        print(f"No UV Mapped tag found for URL: {url}")
        return False
    except Exception as e:
        print(f"Error occurred while checking UV mapping: {e}")
        return False

def download_thing(url):
    if not check_uv_mapping(url):
        print(f"Model at URL {url} is not UV mapped. Skipping download.")
        return

    print(f"Downloading files for URL: {url}")

    raw_directory = '/Users/jungyoonlim/rothko/3d_map/data/raw'
    os.makedirs(raw_directory, exist_ok=True)
    try:
        response = requests.get(url, stream=True)

        if response.status_code != 200:
            print(f"Failed to download from URL {url}. Server responded with status code {response.status_code}.")
            return

        zip_path = f"{raw_directory}/{os.path.basename(url)}.zip"
        with open(zip_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)

        print(f"Successfully downloaded from URL {url}")

    except Exception as e:
        print(f"Error occurred while downloading: {e}")

free_model_urls = get_free_model_urls()
print(f"Found {len(free_model_urls)} free models.")

for model_url in free_model_urls:
    download_thing(model_url)
    time.sleep(random.uniform(1, 3))
