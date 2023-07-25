import os
import zipfile
from zipfile import ZipFile

# Directory where the downloaded .zip files are located
raw_directory = '/Users/jungyoonlim/rothko/3d_map/data/raw' 

# Directory where you want to store the unzipped files
unzipped_directory = '/Users/jungyoonlim/rothko/3d_map/data/unzipped' 

os.makedirs(unzipped_directory, exist_ok=True)  # Ensure the directory exists

for file in os.listdir(raw_directory):
    if file.endswith(".zip"):
        file_path = os.path.join(raw_directory, file)
        thing_id = os.path.splitext(file)[0]  # Get the thing id (filename without extension)

        try:
            with ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(f"{unzipped_directory}/{thing_id}")
            print(f"Successfully unzipped thing {thing_id}")
        except zipfile.BadZipFile:
            print(f"Failed to unzip thing {thing_id}. File is not a zip file.")

def is_zipfile(filename):
    with open(filename, 'rb') as file:
        return file.read(4) == b'PK\x03\x04'
