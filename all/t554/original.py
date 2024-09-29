def quaternionToEuler(x, y, z, w, asDegrees=True):
    """
    Convert a quaternion into an angle

    Cool note: The body of this function was written with chatGPT!!!

    :param x: X component of a quaternion
    :param y: Y component of a quaternion
    :param z: Z component of a quaternion
    :param w: W component of a quaternion
    :param asDegrees: Return the output as degrees. otherwise it will be in radians
    :return: euler angle
    """

    # Calculate the Euler angles
    roll = math.atan2(2 * (w * x + y * z), 1 - 2 * (x ** 2 + y ** 2))
    pitch = math.asin(2 * (w * y - z * x))
    yaw = math.atan2(2 * (w * z + x * y), 1 - 2 * (y ** 2 + z ** 2))

    # Return the Euler angles
    if asDegrees:
        return radToDegree([roll, pitch, yaw])
    return [roll, pitch, yaw]