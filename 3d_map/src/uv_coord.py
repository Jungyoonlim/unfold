import os

def has_uv_coordinates(obj_file_path):
    with open(obj_file_path, 'r') as file:
        for line in file:
            if line.startswith('vt'):
                return True
    return False

directory_path = '/Users/jungyoonlim/rothko/3d_map/data/converted'

# Loop over all files in the directory
for filename in os.listdir(directory_path):
    # Check if the current file is an .obj file
    if filename.endswith('.obj'):
        file_path = os.path.join(directory_path, filename)
        if has_uv_coordinates(file_path):
            print(f'The model {filename} has UV coordinates.')
        else:
            print(f'The model {filename} does not have UV coordinates.')
