import math


def quaternion_to_yaw(quaternion):
    """
    Convert a quaternion into yaw (rotation around the z-axis in radians)
    """
    x, y, z, w = quaternion
    t3 = 2.0 * (w * z + x * y)
    t4 = 1.0 - 2.0 * (y * y + z * z)
    yaw_z = math.atan2(t3, t4)
    return yaw_z


def yaw_difference(quaternion1, quaternion2):
    """
    Calculate the angular difference in yaw between two quaternions, adjusted for the circular nature of angles.

    Args:
    - quaternion1 (tuple): A quaternion (x, y, z, w).
    - quaternion2 (tuple): Another quaternion (x, y, z, w).

    Returns:
    - float: The difference in yaw between the two quaternions, within the range [-pi, pi].
    """
    yaw1 = quaternion_to_yaw(quaternion1)
    yaw2 = quaternion_to_yaw(quaternion2)

    # Calculate the difference and adjust for circular nature of angles
    difference = yaw2 - yaw1
    difference = (difference + math.pi) % (2 * math.pi) - math.pi

    return difference
