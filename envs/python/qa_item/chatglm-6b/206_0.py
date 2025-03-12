
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
    distance_to_center = (x2 - x1) ** 2 + (y2 - y1) ** 2
    
    # Calculate the area of the circle with the smaller radius
    area_circle_ smaller_radius = (r2 * distance_to_center) ** 2
    
    # Calculate the area of the circle with the larger radius
    area_circle_ larger_radius = (r1 * distance_to_center) ** 2
    
    # Calculate the area of the intersection
    intersection_area = area_circle_ smaller_radius - area_circle_ larger_radius
    
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