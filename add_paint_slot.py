# https://www.blender.org/api/blender_python_api_2_78_1/bpy.ops.paint.html?highlight=bpy%20ops%20paint#module-bpy.ops.paint
# https://en.wikibooks.org/wiki/Blender_3D:_Noob_to_Pro/Advanced_Tutorials/Python_Scripting/Addon_User_Interface#Space_Types.2C_Region_Types.2C_Contexts.2C_Oh_My.21

import bpy
from bpy.types import Panel, Operator

bl_info = {
        "name" : "Additional Texture Slots",
        "author" : "Andrew Merizalde <andrewmerizalde@hotmail.com>",
        "version" : (1, 0, 0),
        "blender" : (2, 7, 8),
        "location" : "View 3D > Texture Paint > Tool Shelf > Slots",
        "description" :
            "Add Paint Slots to a Material while in Texture Paint mode. You still have to hook them up in the Node Editor!",
        "warning" : "",
        "wiki_url" : "https://github.com/amerizalde/add_paint_slots",
        "tracker_url" : "",
        "category" : "Paint"}

# add a texture to the active material
class SlotsOperator(Operator):
    # the callback name
    bl_idname = "alm.add_paint_slot"
    bl_label = "..."
    
    def execute(self, context):
        u_color = (
            context.scene.new_texture_color[0],
            context.scene.new_texture_color[1],
            context.scene.new_texture_color[2],
            1.0)
        
        bpy.ops.paint.add_texture_paint_slot(
            type="DIFFUSE_COLOR",
            name=context.scene.new_texture_name,
            width=context.scene.new_texture_width,
            height=context.scene.new_texture_height,
            color=u_color,
            alpha=context.scene.new_texture_alpha,
            float=context.scene.new_texture_float)
        
        self.report({'INFO'}, "Done!")        
        return {"FINISHED"}


# custom Toolshelf Panel
class View3DPanel(Panel):
    """"""
    
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_label = "Add Textures"
    bl_context = "imagepaint"
    bl_category = "Slots"
    
    def draw(self, context):
        
        layout = self.layout        
        row = layout.row()

        obj = context.object
        
        # Display a label
        str_add_slot = "Add another texture to " + obj.name
        row.label(text=str_add_slot)
        
        # properties
        row = layout.row()
        row.prop(context.scene, "new_texture_name")

        row = layout.row()
        row.prop(context.scene, "new_texture_width")

        row = layout.row()
        row.prop(context.scene, "new_texture_height")

        row = layout.row()
        row.prop(context.scene, "new_texture_color")

        row = layout.row()
        row.prop(context.scene, "new_texture_alpha")

        row = layout.row()
        row.prop(context.scene, "new_texture_float")

        # Add a custom operator
        row = layout.row()
        row.operator("alm.add_paint_slot", text="Add Texture", icon="FACESEL_HLT")
        
    
def register():
    bpy.utils.register_class(SlotsOperator)
    bpy.utils.register_class(View3DPanel)
    
    bpy.types.Scene.new_texture_name = bpy.props.StringProperty(
        name="Name",
        description="Describe this texture.",
        default="Texture",
        maxlen=256,
        options={'ANIMATABLE', 'TEXTEDIT_UPDATE'})
        
    bpy.types.Scene.new_texture_width = bpy.props.IntProperty(
        name="Width",
        description="The width of the texture.",
        default=2048,
        step=8,
        options={'ANIMATABLE', 'TEXTEDIT_UPDATE'},
        subtype='PIXEL')

    bpy.types.Scene.new_texture_height = bpy.props.IntProperty(
        name="Height",
        description="The height of the texture.",
        default=2048,
        step=8,
        options={'ANIMATABLE', 'TEXTEDIT_UPDATE'},
        subtype='PIXEL')

    bpy.types.Scene.new_texture_color = bpy.props.FloatVectorProperty(
        name="Color",
        description="Fill color of the texture",
        default=(0.0, 0.0, 0.0),
        min=0.0,
        max=1.0,
        soft_min=0.0,
        soft_max=1.0,
        step=0.001,
        precision=3,
        options={'ANIMATABLE'},
        subtype='COLOR')
        
    bpy.types.Scene.new_texture_alpha = bpy.props.BoolProperty(
        name="Alpha",
        description="Include an alpha channel?",
        default=False)
        
    bpy.types.Scene.new_texture_float = bpy.props.BoolProperty(
        name="32 bit Float",
        description="Create image with 32 bit floating point bit depth.",
        default=False)

    
def unregister():
    bpy.utils.unregister_class(View3DPanel)
    bpy.utils.unregister_class(SlotsOperator)
    
    # remove properties created
    del bpy.types.Scene.new_texture_name
    del bpy.types.Scene.new_texture_width
    del bpy.types.Scene.new_texture_height
    del bpy.types.Scene.new_texture_color
    del bpy.types.Scene.new_texture_alpha
    del bpy.types.Scene.new_texture_float


if __name__ == "__main__":
    register()
