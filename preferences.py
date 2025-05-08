import bpy


def set_basepath(self, value):	
	if '$ObjectName' not in value:
		return
	self["em_basepath"] = value
	

def get_basepath(self):
	try:
		return self["em_basepath"]
	except KeyError:
		return '$SceneDir\\$SceneName_$ObjectName'


class RMKITEXPORTPreferences( bpy.types.AddonPreferences ):
	bl_idname = __package__

	export_manager_basepath: bpy.props.StringProperty(name='BasePath', default='$SceneDir\\$SceneName_$ObjectName', get=get_basepath, set=set_basepath)

	v3d_checkbox: bpy.props.BoolProperty( name="3D View", default=False )
	mesh_checkbox: bpy.props.BoolProperty( name="Mesh", default=False )

	def draw( self, context ):
		layout = self.layout
		layout.prop( self, 'export_manager_basepath', text='Export Manager Path' )
		

def register():
	bpy.utils.register_class( RMKITEXPORTPreferences )


def unregister():
	bpy.utils.unregister_class( 	bpy.utils.register_class( RMKITEXPORTPreferences )
 )