import math

def circle_intersection_area(x1: float, y1: float, r1: float, x2: float, y2: float, r2: float) -> float:
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    if distance >= r1 + r2:
        return 0
    elif distance <= abs(r1 - r2):
        return math.pi * min(r1, r2) ** 2
    
    angle1 = math.acos((r1 ** 2 + distance ** 2 - r2 ** 2) / (2 * r1 * distance))
    angle2 = math.acos((r2 ** 2 + distance ** 2 - r1 ** 2) / (2 * r2 * distance))
    
    area1 = 0.5 * r1 ** 2 * (2 * angle1 - math.sin(2 * angle1))
    area2 = 0.5 * r2 ** 2 * (2 * angle2 - math.sin(2 * angle2))
    
    return area1 + area2
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