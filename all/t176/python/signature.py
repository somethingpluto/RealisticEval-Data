import math
from typing import List


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance_to(self, other: 'Point') -> float:
        """Calculate the Euclidean distance to another point."""
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


def find_k_nearest_neighbors(points: List[Point], query_point: Point, k: int) -> List[Point]:
    """Find the k nearest neighbors to the query_point.

    Args:
        points (List[Point]): A list of Point objects representing the available points in the space.
        query_point (Point): The Point object for which we want to find the nearest neighbors.
        k (int): The number of nearest neighbors to find.

    Returns:
        List[Point]: A list of the k nearest Point objects to the query_point.
    """
