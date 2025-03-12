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
    # Calculate the distance between the centers of the two circles
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    # If the circles do not intersect or one circle is inside the other
    if d >= r1 + r2 or d <= abs(r1 - r2):
        return 0.0
    
    # If one circle is completely inside the other
    if d == 0 and r1 == r2:
        return math.pi * r1 ** 2
    
    # Calculate the area of intersection
    r1_sq = r1 ** 2
    r2_sq = r2 ** 2
    d_sq = d ** 2
    
    # Calculate the angles for the sector areas
    angle1 = math.acos((r1_sq + d_sq - r2_sq) / (2 * r1 * d))
    angle2 = math.acos((r2_sq + d_sq - r1_sq) / (2 * r2 * d))
    
    # Calculate the areas of the sectors
    sector1 = 0.5 * r1_sq * angle1
    sector2 = 0.5 * r2_sq * angle2
    
    # Calculate the areas of the triangles
    triangle1 = 0.5 * r1_sq * math.sin(2 * angle1)
    triangle2 = 0.5 * r2_sq * math.sin(2 * angle2)
    
    # The intersection area is the sum of the sectors minus the triangles
    intersection_area = sector1 + sector2 - triangle1 - triangle2
    
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