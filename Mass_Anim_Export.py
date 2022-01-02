import bpy
path = 'A:\\3D\\base\\'
obj = bpy.context.object
bpy.context.scene.render.engine = 'BLENDER_EEVEE'
for action in bpy.data.actions:
    obj.animation_data.action = bpy.data.actions.get(action.name)
    bpy.context.scene.render.filepath = path + action.name + '\\'
    bpy.ops.render.render(use_viewport = True, write_still=False, animation=True)