import bpy
from mathutils import Vector


def create_cube(coord1: tuple, coord2: tuple):
    """
    Creates a cube in Blender with dimensions and location derived from two diagonal corner coordinates.

    Args:
    coord1 (tuple): The (x, y, z) coordinates of the first corner of the cube.
    coord2 (tuple): The (x, y, z) coordinates of the opposite corner of the cube.
    """
    # Validate input coordinates
    if not (isinstance(coord1, tuple) and isinstance(coord2, tuple)):
        raise TypeError("The coordinates must be provided as tuples.")

    if len(coord1) != 3 or len(coord2) != 3:
        raise ValueError("Both coordinates must have exactly three elements (x, y, z).")

    # Create the base cube with a size of 2 units at the origin
    bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 0))
    cube = bpy.context.active_object

    # Compute the dimensions of the cube based on the coordinates
    dimensions = [abs(coord2[i] - coord1[i]) for i in range(3)]

    # Set the scale of the cube according to the dimensions
    cube.scale = [dimension / 2 for dimension in dimensions]

    # Compute the center of the cube
    center = [(coord1[i] + coord2[i]) / 2 for i in range(3)]

    # Set the location of the cube to the computed center
    cube.location = Vector(center)
