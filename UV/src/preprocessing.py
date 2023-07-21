import os
import requests
import time
import random

def generate_random_ids(n):
    return [random.randint(100000, 999999) for _ in range(n)]

# Generate 30 random 6-digit Thingiverse IDs
thing_id_list = generate_random_ids(15)

def download_thing(thing_id):
    print(f"Downloading files for thing ID: {thing_id}")

    url = f"https://www.thingiverse.com/thing:{thing_id}/zip"

    directory = './downloaded_models'  # The directory where you want to save your files
    os.makedirs(directory, exist_ok=True)  # Ensure the directory exists

    response = requests.get(url, stream=True)

    if response.status_code != 200:
        print(f"Failed to download thing {thing_id}. Server responded with status code {response.status_code}.")
        return

    with open(f"{directory}/{thing_id}.zip", 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
    print(f"Successfully downloaded thing {thing_id}")

print("Starting script...")
print("Downloading files...")

for thing_id in thing_id_list:
    download_thing(thing_id)
    time.sleep(random.uniform(1, 3))  # Delay to avoid overloading the server

print("Script completed successfully.")
