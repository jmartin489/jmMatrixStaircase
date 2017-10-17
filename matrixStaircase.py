import bpy
import math
from mathutils import Matrix
from mathutils import Vector

bpy.ops.object.select_all(action = 'SELECT')
bpy.ops.object.delete()

number_of_stairs = 20

#location of first step
x = 0
y = 0
z = 1

stair_width = 22
stair_depth = 1

staircase_loc_x = 0



for i in range(number_of_stairs):
    translation_vector = Vector([staircase_loc_x, i*2, i])
    scaling_vector = Vector([stair_width, stair_depth, i])
    
    bpy.ops.mesh.primitive_cube_add(location = (x, y, z))
    active_stair = bpy.context.active_object
    active_stair_matrix = bpy.context.object.matrix_world
    active_stair.scale = active_stair_matrix * scaling_vector
    active_stair.location = active_stair_matrix * translation_vector
    