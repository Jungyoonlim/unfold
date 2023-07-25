import os
import trimesh

def convert(input_path, output_path):
    print(f"Converting {input_path} to {output_path}...")
    mesh = trimesh.load_mesh(input_path)
    mesh.export(output_path)
    print(f"Successfully converted {input_path}")

unzipped_directory = '/Users/jungyoonlim/rothko/3d_map/data/unzipped'
converted_directory = '/Users/jungyoonlim/rothko/3d_map/data/converted'
os.makedirs(converted_directory, exist_ok=True)

for thing_id in os.listdir(unzipped_directory):
    thing_path = os.path.join(unzipped_directory, thing_id, "files")

    if os.path.isdir(thing_path):
        for file_name in os.listdir(thing_path):
            if file_name.endswith('.stl'):
                input_path = os.path.join(thing_path, file_name)
                output_path = os.path.join(converted_directory, f'{thing_id}.obj')

                # Convert the STL file to an OBJ file
                convert(input_path, output_path)
