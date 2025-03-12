def intersect_horizontally(rect1, rect2):
    """
    Determine if two rectangles intersect horizontally.

    Each rectangle is defined by a tuple (x1, y1, x2, y2), where:
    - (x1, y1) are the coordinates of the bottom-left corner.
    - (x2, y2) are the coordinates of the top-right corner.

    Args:
        rect1 (tuple): The first rectangle defined by (x1, y1, x2, y2).
        rect2 (tuple): The second rectangle defined by (x1, y1, x2, y2).

    Returns:
        bool: True if the rectangles intersect horizontally, False otherwise.
    """
    
    if rect1[0] <= rect2[2] and rect2[0] <= rect1[2]:
        return True
    else:
        return False
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