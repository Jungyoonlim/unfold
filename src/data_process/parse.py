import numpy as np
import trimesh
import glob

def parse_obj(file_path, grid_size=32):
    print(f"Loading and processing file: {file_path}")
    mesh = trimesh.load_mesh(file_path)
    voxel_grid = mesh.voxelized(pitch=grid_size)
    volume = voxel_grid.matrix
    volume = resize_volume(volume, grid_size)
    return volume

def resize_volume(volume, size):
    # Get the current shape of the volume
    original_shape = volume.shape
    new_volume = np.zeros((size, size, size))
    # Fill the new_volume with the data from the original volume
    for i in range(min(size, original_shape[0])):
        for j in range(min(size, original_shape[1])):
            for k in range(min(size, original_shape[2])):
                new_volume[i, j, k] = volume[i, j, k]
    return new_volume

obj_file_path = glob.glob('/Users/jungyoonlim/rothko/3d_map/data/converted/*.obj')

X = []
for file_path in obj_file_path:
    volume = parse_obj(file_path)
    X.append(volume)
    print(f"Currently loaded {len(X)} files.")

# Convert list to numpy array
X = np.array(X, dtype=np.float32)
print(f"Data loaded successfully, array shape: {X.shape}")

