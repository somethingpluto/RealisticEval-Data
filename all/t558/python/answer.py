import math

def degrees_to_radians(degrees):
    """
    Convert an angle from degrees to radians.

    :param degrees: The angle in degrees to convert.
    :return: The angle in radians.
    """
    radians = degrees * (math.pi / 180)
    return radians