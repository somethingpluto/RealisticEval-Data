def degreeToRad(angle):
    """
    Convert an angle from degrees to radians

    :param angle: angle in degrees
    :return: angle in radians
    """
    return [degree * (pi / 180) for degree in angle]
