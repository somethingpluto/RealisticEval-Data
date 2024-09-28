def is_point_inside_triangle(px: float, py: float, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float):
    """
    Check if a point is inside a triangle defined by three vertices.

    Args:
        px (float): The x-coordinate of the point to check.
        py (float): The y-coordinate of the point to check.
        x1 (float): The x-coordinate of the first vertex of the triangle.
        y1 (float): The y-coordinate of the first vertex of the triangle.
        x2 (float): The x-coordinate of the second vertex of the triangle.
        y2 (float): The y-coordinate of the second vertex of the triangle.
        x3 (float): The x-coordinate of the third vertex of the triangle.
        y3 (float): The y-coordinate of the third vertex of the triangle.

    Returns:
        bool: True if the point (px, py) is inside or on the edge of the triangle formed by the vertices (x1, y1), (x2, y2), (x3, y3); False otherwise.
    """
