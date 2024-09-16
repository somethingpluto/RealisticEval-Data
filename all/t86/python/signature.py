from typing import List


def bresenham_line(x1: int, y1: int, x2: int, y2: int) -> List[tuple]:
    """
    Generates integer coordinates on the line from (x1, y1) to (x2, y2) using Bresenham's line algorithm.

    Bresenham's algorithm calculates the points of an approximately straight line between two given points on a grid.
    It is particularly well-suited for computer graphics where an efficient, integer-based algorithm is needed to
    determine which points should be rasterized to represent the line.

    Args:
        x1 (int): The x-coordinate of the starting point of the line.
        y1 (int): The y-coordinate of the starting point of the line.
        x2 (int): The x-coordinate of the ending point of the line.
        y2 (int): The y-coordinate of the ending point of the line.

    Returns:
        list of tuples: A list where each tuple contains the x and y coordinates of a point on the line.
    """
