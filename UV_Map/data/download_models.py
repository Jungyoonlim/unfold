import requests
import os
import zipfile
import io

'''
download the first model returned by the search API
then save it as a .zip file in the ./models 
then extract the files from the .zip file into the same folder
'''

API_token = '5819940972cb4a2f9bc873aaa8329977'
download_folder = './models'

os.makedirs(download_folder, exist_ok=True)

# use the search api to find models
search_url = f'https://api.sketchfab.com/v3/search?type=models&max_face_count=10000'
response = requests.get(search_url, headers={'Authorization': f'Token {API_token}'})
response.raise_for_status()

# Get the first result
model_uid = response.json()['results'][0]['uid']

# Use the download API to get the download link
download_url = f'https://api.sketchfab.com/v3/models'
response = requests.get(download_url, headers={'Authorization': f'Token {API_token}'})
response.raise_for_status()

# Download the file
file_url = response.json()['gltf']['url']
response = requests.get(file_url)
response.raise_for_status()

# Save the file to disk
file_path = os.path.join(download_folder, f'{model_uid}.zip')
with open(file_path, 'wb') as f:
    f.write(response.content)

# Unzip the file
with zipfile.ZipFile(file_path, 'r') as zip_ref:
    zip_ref.extractall(download_folder)