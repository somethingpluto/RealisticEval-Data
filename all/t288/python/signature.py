from typing import List, Tuple


def bresenham_line(x1: int, y1: int, x2: int, y2: int) -> List[Tuple[int, int]]:
    """
    use Bresenham line algorithm  generate a straight line between two points, returning all the points that the line passes through
    Args:
        x1 (int):  Coordinates of the start point x.
        y1 (int):  Coordinates of the start point y.
        x2 (int):  Coordinates of the end point x.
        y2 (int):  Coordinates of the start point y.

    Returns:
        list of tuples: A list of points (tuples of x and y coordinates) that the line passes through.
    """
