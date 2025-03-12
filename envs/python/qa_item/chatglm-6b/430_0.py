
def intersect_vertically(rect1, rect2):
    if not (rect1 == rect2 or rect1[-1] == rect2[-1]):
        return False
    for i in range(len(rect1)):
        if not (rect1[i] == rect2[i] or rect1[i-1] == rect2[i-1]):
            return False
    return True

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