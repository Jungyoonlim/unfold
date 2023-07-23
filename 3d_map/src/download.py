from bs4 import BeautifulSoup
import requests
import random
import os  # Add this import

def generate_random_ids(n):
    return [random.randint(100000, 999999) for _ in range(n)]

thing_id_list = generate_random_ids(100)

def check_uv_mapping(thing_id):
    url = f"https://www.turbosquid.com/3d-models/3d-model-{thing_id}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find UV Mapped tag using its ID
    uv_mapped_tag = soup.find('span', {'id': 'FPSpec_uv_mapped'}) 

    #find free ones!
    free_tag = soup.find('span', {'id': 'price'})

    if uv_mapped_tag is not None:
        print(f"UV Mapped tag found for Thing ID: {thing_id}")
        return True

    print(f"No UV Mapped tag found for Thing ID: {thing_id}")
    return False

def download_thing(thing_id):
    print(f"Downloading files for thing ID: {thing_id}")

    url = f"https://www.turbosquid.com/3d-models/3d-model-{thing_id}"

    raw_directory = '/Users/jungyoonlim/rothko/3d_map/data/raw'
    os.makedirs(raw_directory, exist_ok=True)  # 'os' is now recognized  
    response = requests.get(url, stream=True)

    if response.status_code != 200:
        print(f"Failed to download thing {thing_id}. Server responded with status code {response.status_code}.")
        return

    zip_path = f"{raw_directory}/{thing_id}.zip"
    with open(zip_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)

    print(f"Successfully downloaded thing {thing_id}")

for thing_id in thing_id_list:
    if check_uv_mapping(thing_id):
        download_thing(thing_id)
