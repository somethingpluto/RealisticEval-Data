def get_line(from_pt, to_pt):
    # Bresenham's line algorithm
    # written by GPT-3
    # from_pt and to_pt are tuples of the form (x, y)
    # returns a list of points that the line passes through

    x1, y1 = from_pt
    x2, y2 = to_pt
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    steep = dy > dx

    if steep:
        x1, y1 = y1, x1  # Swap x and y
        x2, y2 = y2, x2  # Swap x and y

    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    dx = x2 - x1
    dy = y2 - y1
    error = dx // 2

    y_step = 1 if y1 < y2 else -1
    y = y1

    points = []
    for x in range(x1, x2 + 1):
        coord = (y, x) if steep else (x, y)
        points.append(coord)
        error -= abs(dy)

        if error < 0:
            y += y_step
            error += dx

    return points