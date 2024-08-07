# CREATED BY CHATGPT
def find_intersection(line1, line2):
    x1, y1, x2, y2 = line1
    x3, y3, x4, y4 = line2

    # Calculate the direction vectors of the two line segments
    dx1 = x2 - x1
    dy1 = y2 - y1
    dx2 = x4 - x3
    dy2 = y4 - y3

    # Calculate determinant to check if the lines are parallel
    determinant = dx1 * dy2 - dx2 * dy1

    # Check if the lines are parallel (determinant is close to 0)
    if abs(determinant) < 1e-10:
        return None  # No intersection, the lines are parallel

    # Calculate the parameters for the intersection point
    t1 = ((x3 - x1) * dy2 - (y3 - y1) * dx2) / determinant
    t2 = ((x3 - x1) * dy1 - (y3 - y1) * dx1) / determinant

    # Check if the intersection point lies within both line segments
    if 0 <= t1 <= 1 and 0 <= t2 <= 1:
        x = x1 + t1 * dx1
        y = y1 + t1 * dy1
        return x, y
    else:
        return None  # Intersection point is outside the line segments