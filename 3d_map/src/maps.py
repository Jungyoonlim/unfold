import bpy

def generate_uv_map(obj_name):
    obj = bpy.data.objects[obj_name]
    bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=0.001)