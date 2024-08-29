from typing import Tuple


def calculate_euclidean_distance(point1: Tuple[float, float], point2: Tuple[float, float]) -> float:
    """
    Calculate the Euclidean distance between two points in a 2D space.

    Args:
        point1 (Tuple[float, float]): The first point as a tuple of coordinates (x1, y1).
        point2 (Tuple[float, float]): The second point as a tuple of coordinates (x2, y2).

    Returns:
        float: The Euclidean distance between the two points.

    """
    if not (isinstance(point1, tuple) and isinstance(point2, tuple)):
        raise TypeError("Both points must be tuples")

    if not (len(point1) == 2 and len(point2) == 2):
        raise TypeError("Both points must be tuples of two elements")

    if not (all(isinstance(coord, (int, float)) for coord in point1) and
            all(isinstance(coord, (int, float)) for coord in point2)):
        raise TypeError("All coordinates must be integers or floats")

    # Extract coordinates from the input tuples
    x1, y1 = point1
    x2, y2 = point2

    # Compute differences and Euclidean distance using the Pythagorean theorem
    dx = x2 - x1
    dy = y2 - y1

    return (dx ** 2 + dy ** 2) ** 0.5
