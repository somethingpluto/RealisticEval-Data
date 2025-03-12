import math

def intersect_vertically(rect1, rect2):
    """
    Check whether two rectangles intersect in the vertical direction

    Each rectangle is defined by a tuple (x1, y1, x2, y2), where:
    - (x1, y1) are the coordinates of the bottom-left corner.
    - (x2, y2) are the coordinates of the top-right corner.

    Args:
        rect1 (tuple): The first rectangle defined by (x1, y1, x2, y2).
        rect2 (tuple): The second rectangle defined by (x1, y1, x2, y2).

    Returns:
        bool: True if the rectangles intersect vertically, False otherwise.
    """
    if max(rect1[0], rect2[0]) < min(rect1[2], rect2[2]):
        return True
    else:
        return False
import unittest


class TestIntersectVertically(unittest.TestCase):

    def test_case1(self):
        """Test with overlapping rectangles."""
        rect1 = (0, 0, 2, 2)
        rect2 = (1, 1, 3, 3)
        self.assertTrue(intersect_vertically(rect1, rect2))

    def test_case2(self):
        """Test with overlapping rectangles."""
        rect1 = (-1, -1, 1, 1)
        rect2 = (0, 0, 2, 2)
        self.assertTrue(intersect_vertically(rect1, rect2))

    def test_case3(self):
        # Test case where rectangles partially overlap vertically
        rect1 = (0, 1, 2, 4)
        rect2 = (1, 0, 3, 2)
        self.assertTrue(intersect_vertically(rect1, rect2))

    def test_case4(self):
        # Test case where rectangles are identical
        rect1 = (0, 0, 2, 2)
        rect2 = (0, 0, 2, 2)
        self.assertTrue(intersect_vertically(rect1, rect2))

    def test_case5(self):
        # Test case where one rectangle is completely inside the other
        rect1 = (0, 0, 4, 4)
        rect2 = (1, 1, 2, 2)
        self.assertTrue(intersect_vertically(rect1, rect2))

if __name__ == '__main__':
    unittest.main()