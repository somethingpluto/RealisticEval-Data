# CREATED BY CHATGPT
from typing import Tuple


def distance_between_points(point1: Tuple[float, float], point2: Tuple[float, float]) -> float:

    # Extract coordinates from the input tuples
    x1, y1 = point1
    x2, y2 = point2

    # Compute differences and Euclidean distance using the Pythagorean theorem
    dx = x2 - x1
    dy = y2 - y1

    return (dx ** 2 + dy ** 2) ** 0.5