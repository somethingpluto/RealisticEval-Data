def bresenham_line(x1, y1, x2, y2):
    """Generates integer coordinates on the line from (x1, y1) to (x2, y2) using Bresenham's line algorithm."""
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
        if e2 >= dy:  # e_xy+e_x > 0
            err += dy
            x1 += sx
        if e2 <= dx:  # e_xy+e_y < 0
            err += dx
            y1 += sy

    return points