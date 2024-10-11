import math

def radians_to_degrees(radians):
    """
    Convert an angle from radians to degrees.

    :param radians: The angle in radians to convert.
    :return: The angle in degrees.
    """
    degrees = radians * (180 / math.pi)
    return degrees