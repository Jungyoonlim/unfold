import bpy
import os

def load_obj(obj_path):
    # Clear all mesh objects
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.object.select_by_type(type='MESH')
    bpy.ops.object.delete()

    # Load the new object
    bpy.ops.import_scene.obj(filepath=obj_path)
    
    # Return the name of the loaded object
    return bpy.context.selected_objects[0].name

def generate_uv_map(obj_name):
    obj = bpy.data.objects[obj_name]
    bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=0.001)

    # Export the UV layout
    uv_output_path = os.path.join(os.path.dirname(obj_path), obj_name + ".png")
    bpy.ops.uv.export_layout(filepath=uv_output_path)

# Example usage:
obj_path = '/Users/jungyoonlim/rothko/3d_map/data/converted'  
obj_name = load_obj(obj_path)
generate_uv_map(obj_name)

try:
    import bpy
except ImportError:
    pass 