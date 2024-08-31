from typing import List


def is_point_in_polygon(point: tuple, polygon: List[tuple]) -> bool:
    """
    Determine if the point (x, y) is inside the given polygon.
    The polygon is defined as a list of tuples (x, y) representing the vertices.

    Args:
    point: A tuple (x, y) representing the point to check.
    polygon: A list of tuples (x, y) representing the vertices of the polygon.

    Returns:
    bool: True if the point is inside the polygon, False otherwise.
    """
