def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    calculate the distance between two points on the earth based on their latitude and longitude
    Args:
        lat1 (float): Latitude of the first point in degrees.
        lon1 (float): Longitude of the first point in degrees.
        lat2 (float): Latitude of the second point in degrees.
        lon2 (float): Longitude of the second point in degrees.

    Returns:
        Distance between the two points in kilometers.
    """