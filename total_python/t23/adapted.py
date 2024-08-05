def get_line_segment_intersection(seg1, seg2):
    # Unpack segment points
    (x1, y1), (x2, y2) = seg1
    (x3, y3), (x4, y4) = seg2

    # Compute direction vectors and determinant
    dx1, dy1 = x2 - x1, y2 - y1
    dx2, dy2 = x4 - x3, y4 - y3
    determinant = dx1 * dy2 - dx2 * dy1

    # Check for parallel lines
    if abs(determinant) < 1e-10:
        return None

    # Calculate intersection parameters
    t1 = ((x3 - x1) * dy2 - (y3 - y1) * dx2) / determinant
    t2 = ((x3 - x1) * dy1 - (y3 - y1) * dx1) / determinant

    # Determine if the intersection is within both segments
    if 0 <= t1 <= 1 and 0 <= t2 <= 1:
        return x1 + t1 * dx1, y1 + t1 * dy1
    return None
