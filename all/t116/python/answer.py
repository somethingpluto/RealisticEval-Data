def toroidal_diff(this_point, other_point, width, height):
    dx = this_point['x'] - other_point['x']
    dy = this_point['y'] - other_point['y']

    # Handle wraparound for the x dimension
    if abs(dx) > width / 2:
        dx = dx - width if dx > 0 else dx + width

    # Handle wraparound for the y dimension
    if abs(dy) > height / 2:
        dy = dy - height if dy > 0 else dy + height

    return [dx, dy]