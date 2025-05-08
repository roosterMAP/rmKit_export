bl_info = {
	"name": "rmKit_export",
	"author": "Timothee Yeramian",
	"location": "View3D > Sidebar",
	"description": "Export Manager for modular kit based workflows",
	"category": "",
	"blender": ( 4, 0, 0 ),
	"warning": "",
	"doc_url": "https://rmkit.readthedocs.io/en/latest/",
}

import bpy


class rmKitExportPannel_parent( bpy.types.Panel ):
	bl_idname = "VIEW3D_PT_RMKITEXPORT_PARENT"
	bl_label = "rmExportManager"
	bl_space_type = "VIEW_3D"
	bl_region_type = "UI"
	bl_category = "rmExportManager"

	def draw( self, context ):
		layout = self.layout


from . import (
	preferences,
	exportmanager,
)


def register():
	bpy.utils.register_class( rmKitExportPannel_parent )
	preferences.register()
	exportmanager.register()

def unregister():
	bpy.utils.unregister_class( rmKitExportPannel_parent )
	preferences.unregister()
	exportmanager.unregister()