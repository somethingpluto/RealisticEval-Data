def calculate_haversine_distance(latitude1: float, longitude1: float, latitude2: float, longitude2: float) -> float:
    """
    Calculates the great-circle distance between two points on the Earth
    using their latitude and longitude based on the Haversine formula.

    Args:
        latitude1 (float): Latitude of the first point in degrees.
        longitude1 (float): Longitude of the first point in degrees.
        latitude2 (float): Latitude of the second point in degrees.
        longitude2 (float): Longitude of the second point in degrees.

    Returns:
        float: The distance between the two points in kilometers.
    """