import math

def circle_intersection_area(x1: float, y1: float, r1: float, x2: float, y2: float, r2: float) -> float:
    # Calculate the distance between the centers of the two circles
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    # Check if the circles are completely separate
    if distance >= r1 + r2:
        return 0.0
    
    # Check if one circle is completely inside the other
    if distance <= abs(r1 - r2):
        return math.pi * min(r1, r2)**2
    
    # Calculate the intersection area using trigonometry
    angle1 = math.acos((r1**2 + distance**2 - r2**2) / (2 * r1 * distance))
    angle2 = math.acos((r2**2 + distance**2 - r1**2) / (2 * r2 * distance))
    
    sector_area1 = 0.5 * angle1 * r1**2
    sector_area2 = 0.5 * angle2 * r2**2
    
    triangle_area1 = r1 * math.sin(angle1) * distance / 2
    triangle_area2 = r2 * math.sin(angle2) * distance / 2
    
    intersection_area = sector_area1 + sector_area2 - triangle_area1 - triangle_area2
    
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