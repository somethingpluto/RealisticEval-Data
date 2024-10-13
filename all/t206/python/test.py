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
