def intersect_horizontally(rect1, rect2):
    x1, y1, x2, y2 = rect1
    x3, y3, x4, y4 = rect2

    # Check if the rectangles have overlapping x-coordinates
    return (x1 < x4 and x2 > x3) or (x3 < x1 and x4 > x2)
import unittest


class TestIntersectHorizontally(unittest.TestCase):

    def test_case1(self):
        """Test with overlapping rectangles."""
        rect1 = (0, 0, 2, 2)
        rect2 = (1, 1, 3, 3)
        self.assertTrue(intersect_horizontally(rect1, rect2))

    def test_case2(self):
        """Test with rectangles touching at a point (not overlapping)."""
        rect1 = (0, 0, 1, 1)
        rect2 = (1, 1, 2, 2)
        self.assertTrue(intersect_horizontally(rect1, rect2))

    def test_case3(self):
        """Test with adjacent rectangles (no overlap)."""
        rect1 = (0, 0, 2, 2)
        rect2 = (2, 0, 3, 3)
        self.assertTrue(intersect_horizontally(rect1, rect2))

    def test_case4(self):
        """Test with one rectangle fully inside another."""
        rect1 = (1, 1, 4, 4)
        rect2 = (2, 2, 3, 3)
        self.assertTrue(intersect_horizontally(rect1, rect2))

    def test_case5(self):
        """Test with overlapping rectangles."""
        rect1 = (-1, -1, 1, 1)
        rect2 = (0, 0, 2, 2)
        self.assertTrue(intersect_horizontally(rect1, rect2))

if __name__ == '__main__':
    unittest.main()