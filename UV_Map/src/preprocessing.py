import os 
import requests
from bs4 import BeautifulSoup
import time
import random
from zipfile import ZipFile 
import trimesh

def preprocess_model(model_path):
    mesh = trimesh.load_mesh(model_path)
    mesh.apply_scale(1.0/mesh.extents.max())
    mesh.export(model_path)

print("Starting script...")

base_url = "https://archive.org/details/thingiverse"

response = requests.get(base_url)

soup = BeautifulSoup(response.text, 'html.parser')

links = soup.find_all('a')

# filter the links to get only those that point to ZIP files
zip_links = [link['href'] for link in links if link['href'].endswith('.zip')]

print("Downloading files...")

# download the first 500 zip files
for zip_link in zip_links[:500]:
    # The zip_link might be a relative URL, so we use urljoin to make it an absolute URL
    full_url = requests.compat.urljoin(base_url, zip_link)

     # Download the ZIP file
    zip_data = requests.get(full_url).content
    print(f"Downloaded file: {os.path.basename(zip_link)}")

    # Save it to downloaded_models
    save_path = os.path.join('./downloaded_models', os.path.basename(zip_link))
    with open(save_path, 'wb') as f:
        f.write(zip_data)

    # Unzip the file
    with ZipFile(save_path, 'r') as zip_ref:
        zip_ref.extractall('./unzipped_models')

    model_files = os.listdir('./unzipped_models')
    for model_file in model_files:
        preprocess_model(os.path.join('./unzipped_models', model_file))
        
    # Delay to avoid overloading the server
    time.sleep(random.uniform(1, 3))

print("Script completed successfully.")
