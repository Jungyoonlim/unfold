import os
import pymesh

def convert(input_path, output_path):
    mesh  = pymesh.load_mesh(input_path)
    pymesh.save_mesh(output_path, mesh)

unzipped_directory = '/Users/jungyoonlim/rothko/UV/data/unzipped'
converted_directory = '/Users/jungyoonlim/rothko/UV/data/converted'
os.makedirs(converted_directory, exist_ok=True)

for thing_id in os.listdir(unzipped_directory):
    thing_path = os.path.join(unzipped_directory, thing_id, "files")


