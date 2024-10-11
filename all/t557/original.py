def radToDegree(angle):
    """
    Convert an angle from radians to degrees

    :param angle: angle in radians
    :return: angle in degrees
    """
    return [rad * 180 / math.pi for rad in angle]