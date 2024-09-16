def bresenham_line(x1, y1, x2, y2):
    """
    Generate points of a line using Bresenham's line algorithm between two points.

    Args:
    x1, y1: Coordinates of the start point.
    x2, y2: Coordinates of the end point.

    Returns:
    list of tuples: A list of points (tuples of x and y coordinates) that the line passes through.
    """
    points = []
    dx = abs(x2 - x1)
    dy = -abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx + dy  # error value e_xy

    while True:
        points.append((x1, y1))
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        # horizontal step
        if e2 >= dy:
            if x1 == x2:
                break
            err += dy
            x1 += sx
        # vertical step
        if e2 <= dx:
            if y1 == y2:
                break
            err += dx
            y1 += sy

    return points
