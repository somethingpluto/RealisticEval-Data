from math import acos, sqrt, pi

def circle_intersection_area(x1: float, y1: float, r1: float, x2: float, y2: float, r2: float) -> float:
    """
    Calculate the intersection area of two circles. Each circle is defined by its center coordinates and radius.

    Args:
        x1 (float): The x-coordinate of the center of the first circle.
        y1 (float): The y-coordinate of the center of the first circle.
        r1 (float): The radius of the first circle.
        x2 (float): The x-coordinate of the center of the second circle.
        y2 (float): The y-coordinate of the center of the second circle.
        r2 (float): The radius of the second circle.

    Returns:
        float: The area of the intersection between the two circles.
    """
    # Calculate the distance between the centers of the two circles
    d = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    # If the circles do not intersect, the intersection area is 0
    if d >= r1 + r2:
        return 0.0

    # If one circle is completely inside the other, the intersection area is the area of the smaller circle
    if d <= abs(r1 - r2):
        return pi * min(r1, r2) ** 2

    # Calculate the intersection area using the formula
    a = (r1 ** 2 * acos((d ** 2 + r1 ** 2 - r2 ** 2) / (2.0 * d * r1))) + (r2 ** 2 * acos((d ** 2 + r2 ** 2 - r1 ** 2) / (2.0 * d * r2))) - (0.5 * sqrt((-d + r1 + r2) * (d + r1 - r2) * (d - r1 + r2) * (d + r1 + r2)))
    return a
import unittest


class Tester(unittest.TestCase):

    def test_circle_intersection_area(self):
        tolerance = 1e-5

        # No overlap, circles far apart
        self.assertAlmostEqual(circle_intersection_area(0.0, 0.0, 3.0, 10.0, 10.0, 3.0), 0.0, delta=tolerance)

        # No overlap, circles just touching
        self.assertAlmostEqual(circle_intersection_area(0.0, 0.0, 3.0, 6.0, 0.0, 3.0), 0.0, delta=tolerance)

        # One circle inside the other
        area = circle_intersection_area(0.0, 0.0, 5.0, 2.0, 0.0, 3.0)
        self.assertAlmostEqual(area, 28.2743, delta=tolerance)  # Area of smaller circle

        # Identical circles, full overlap
        area = circle_intersection_area(0.0, 0.0, 3.0, 0.0, 0.0, 3.0)
        self.assertAlmostEqual(area, 28.2743, delta=tolerance)  # Area of one circle

if __name__ == '__main__':
    unittest.main()