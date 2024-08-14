def is_point_in_polygon(point, polygon):
    """
    Determine if the point (x, y) is inside the given polygon.
    The polygon is defined as a list of tuples (x, y) representing the vertices.

    Args:
    point: A tuple (x, y) representing the point to check.
    polygon: A list of tuples (x, y) representing the vertices of the polygon.

    Returns:
    bool: True if the point is inside the polygon, False otherwise.
    """

    x, y = point
    inside = False
    n = len(polygon)
    p1x, p1y = polygon[0]

    for i in range(n + 1):
        p2x, p2y = polygon[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y

    return inside