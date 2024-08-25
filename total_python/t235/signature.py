def calculate_bearing(lat1: float, lon1: float, lat2: float, lon2: float) -> int:
    """
    calculate the azimuth between two points on the earth. This function accepts the latitude and longitude of the two points as a parameter and returns the azimuth from the first point to the second point in degrees
    Args:
        lat1 (float): Latitude of the starting point in decimal degrees.
        lon1 (float): Longitude of the starting point in decimal degrees.
        lat2 (float): Latitude of the ending point in decimal degrees.
        lon2 (float): Longitude of the ending point in decimal degrees.

    Returns:
        float: Bearing in degrees from the starting point to the ending point, ranging from 0 to 360.
    """
