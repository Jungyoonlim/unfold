import trimesh

def load_model(file_path):
    mesh = trimesh.load_mesh(file_path)
    return mesh
