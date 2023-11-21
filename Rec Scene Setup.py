bl_info = {
    "name": "Rec Scene Setup",
    "author": "Pacifiky",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > N",
    "description": "Sets up Scene for you",
    "warning": "",
    "doc_url": "",
    "category": "Scene",
}


import bpy
from bpy.types import (Operator, Panel)

class cycles(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "cycles.1"
    bl_label = "Simple Object Operator"

    def execute(self, context):
        bpy.context.scene.render.engine = 'CYCLES'
        bpy.context.scene.cycles.device = 'GPU'
        bpy.context.scene.cycles.samples = 200
        bpy.context.scene.cycles.max_bounces = 3
        bpy.context.scene.cycles.use_fast_gi = True
        bpy.context.scene.render.use_motion_blur = True
        bpy.context.scene.render.use_simplify = True
        bpy.context.scene.view_settings.look = 'Very High Contrast'
        bpy.context.scene.render.use_persistent_data = True
        bpy.context.scene.cycles.use_guiding = True
        return {'FINISHED'}
class eevee(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "eevee.1"
    bl_label = "Simple Object Operator"

    def execute(self, context):
        bpy.context.scene.render.engine = 'BLENDER_EEVEE'
        bpy.context.scene.eevee.use_gtao = True
        bpy.context.scene.eevee.use_bloom = True
        bpy.context.scene.eevee.use_ssr = True
        bpy.context.scene.eevee.use_motion_blur = True
        bpy.context.scene.view_settings.look = 'Very High Contrast'
        bpy.context.scene.render.use_simplify = True
        return {'FINISHED'}

class THD(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "eevee.1"
    bl_label = "Simple Object Operator"

    def execute(self, context):
        bpy.context.scene.render.resolution_x = 1920
        bpy.context.scene.render.resolution_y = 1080
        return {'FINISHED'}

class HD(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "hd.1"
    bl_label = "Simple Object Operator"

    def execute(self, context):
        bpy.context.scene.render.resolution_x = 1280
        bpy.context.scene.render.resolution_y = 720
        return {'FINISHED'}
        
class Tr(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "tr.1"
    bl_label = "Simple Object Operator"

    def execute(self, context):
        bpy.context.scene.render.film_transparent = True
        return {'FINISHED'}
    
class dele(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "dele.1"
    bl_label = "Simple Object Operator"

    def execute(self, context):
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False, confirm=False)
        return {'FINISHED'}
    
class ac(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "acc.1"
    bl_label = "Simple Object Operator"

    def execute(self, context):
        bpy.context.object.location[2] = 3
        bpy.context.object.rotation_euler[2] = 3.14159
        return {'FINISHED'}

class Panel(bpy.types.Panel):
    bl_label = "Rec Scene"
    bl_idname = "OBJECT_PT_rec"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Rec Scene"

    def draw(self, context):
        layout = self.layout
        obj = context.object
        layout.label(text="Setup Scene")
        row = layout.row()
        row.operator(cycles.bl_idname, text="Cycles", icon='ANTIALIASED')
        row.operator(eevee.bl_idname, text="EEVEE", icon='ALIASED')
        layout.label(text="Resolutions")
        row = layout.row()
        row.scale_y = 2.0
        row.operator(THD.bl_idname, text="True HD", icon='ANTIALIASED')
        row.operator(HD.bl_idname, text="HD", icon='ALIASED')
        layout.label(text="Misc")
        row = layout.row()
        row.scale_y = 3.0
        row.operator(Tr.bl_idname, text="Transparent", icon='SELECT_SET')
        row.operator(dele.bl_idname, text="Delete All", icon='CANCEL')
        layout.label(text="RIG")
        row = layout.row()
        row.scale_y = 3.0
        row.operator(ac.bl_idname, text="Setup Accsessories", icon='MOD_CLOTH')
        layout.label(text="Made by Pacifiky")
        
from bpy.utils import register_class, unregister_class

_classes = [
    cycles,
    Panel,
    eevee,
    THD,
    HD,
    Tr,
    dele,
    ac
]

def register():
    for cls in _classes:
        register_class(cls)


def unregister():
     for cls in _classes:
        unregister_class(cls)

if __name__ == "__main__":
    register()
