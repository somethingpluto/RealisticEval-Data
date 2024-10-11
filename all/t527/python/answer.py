def area(x1, y1, x2, y2, x3, y3):
    """Calculate the area of a triangle given by its vertices."""
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)


def is_point_inside_triangle(px, py, x1, y1, x2, y2, x3, y3):
    """Check if a point (px, py) is inside the triangle formed by (x1, y1), (x2, y2), (x3, y3)."""
    # Calculate the area of the triangle ABC
    A = area(x1, y1, x2, y2, x3, y3)

    # Calculate the area of the triangle PAB, PBC, and PCA
    A1 = area(px, py, x1, y1, x2, y2)
    A2 = area(px, py, x2, y2, x3, y3)
    A3 = area(px, py, x3, y3, x1, y1)

    # Check if the sum of A1, A2, and A3 is equal to A
    return A == A1 + A2 + A3