import math

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
    distance_between_centers = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    if distance_between_centers >= r1 + r2:
        return 0

    if distance_between_centers <= abs(r1 - r2):
        return math.pi * min(r1, r2) ** 2

    angle1 = 2 * math.acos((r1 ** 2 + distance_between_centers ** 2 - r2 ** 2) / (2 * r1 * distance_between_centers))
    angle2 = 2 * math.acos((r2 ** 2 + distance_between_centers ** 2 - r1 ** 2) / (2 * r2 * distance_between_centers))
    
    area1 = 0.5 * angle1 * r1 ** 2 - 0.5 * r1 ** 2 * math.sin(angle1)
    area2 = 0.5 * angle2 * r2 ** 2 - 0.5 * r2 ** 2 * math.sin(angle2)
    
    intersection_area = area1 + area2
    return intersection_area
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