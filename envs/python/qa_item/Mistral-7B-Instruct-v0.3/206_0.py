import math

def circle_intersection_area(x1, y1, r1, x2, y2, r2):
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
    # Calculate the distance between the centers of the circles
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    # If the distance between the centers is greater than the sum of the radii, the circles do not intersect
    if distance > r1 + r2:
        return 0

    # Calculate the radius of the circle that represents the intersection area
    intersection_radius = math.sqrt(r1**2 - ((r1**2 - r2**2 + distance**2)/2))

    # Calculate the area of the intersection
    area = math.pi * intersection_radius**2

    return area
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