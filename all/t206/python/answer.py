import math


def circle_intersection_area(x1, y1, r1, x2, y2, r2):
    PI = 3.141592653589793
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    # If the circles do not overlap
    if d >= r1 + r2:
        return 0.0

    # If one circle is completely within the other
    if d <= abs(r1 - r2):
        r = min(r1, r2)
        return PI * r * r

    r1_sq = r1 ** 2
    r2_sq = r2 ** 2

    alpha = math.acos((r1_sq + d ** 2 - r2_sq) / (2 * r1 * d)) * 2
    beta = math.acos((r2_sq + d ** 2 - r1_sq) / (2 * r2 * d)) * 2

    area1 = 0.5 * r1_sq * (alpha - math.sin(alpha))
    area2 = 0.5 * r2_sq * (beta - math.sin(beta))

    return area1 + area2