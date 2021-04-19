import bpy
 
# Settings
name = 'Gridtastic'
rows = 5
columns = 10

verts = []
faces = []
 
# Create Mesh Datablock
mesh = bpy.data.meshes.new(name)
mesh.from_pydata(verts, [], faces)
 
# Create Object and link to scene
obj = bpy.data.objects.new(name, mesh)
bpy.context.collection.objects.link(obj)
 
# Select the object
bpy.context.scene.objects.active = obj
obj.select = True