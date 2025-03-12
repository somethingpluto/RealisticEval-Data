import math

def intersect_vertically(rect1, rect2):
    x1_rect1, y1_rect1, x2_rect1, y2_rect1 = rect1
    x1_rect2, y1_rect2, x2_rect2, y2_rect2 = rect2
    
    if y2_rect1 >= y1_rect2 and y2_rect1 <= y2_rect2:
        return True
    elif y1_rect1 >= y1_rect2 and y1_rect1 <= y2_rect2:
        return True
    elif y1_rect2 >= y1_rect1 and y1_rect2 <= y2_rect1:
        return True
    elif y2_rect2 >= y1_rect1 and y2_rect2 <= y2_rect1:
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