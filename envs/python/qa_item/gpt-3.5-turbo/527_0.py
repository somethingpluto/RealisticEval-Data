import math

def is_point_inside_triangle(px: float, py: float, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float) -> bool:
    def sign(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float) -> float:
        return (x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3)
    
    b1 = sign(px, py, x1, y1, x2, y2) < 0.0
    b2 = sign(px, py, x2, y2, x3, y3) < 0.0
    b3 = sign(px, py, x3, y3, x1, y1) < 0.0
    
    return ((b1 == b2) and (b2 == b3))
import unittest


class TestPointInsideTriangle(unittest.TestCase):

    def test_point_inside_triangle(self):
        """Test case where point is inside the triangle."""
        triangle_vertices = (0, 0, 5, 0, 2.5, 5)
        point = (2.5, 2)  # Inside the triangle
        self.assertTrue(is_point_inside_triangle(point[0], point[1], *triangle_vertices))

    def test_point_on_edge(self):
        """Test case where point is on the edge of the triangle."""
        triangle_vertices = (0, 0, 5, 0, 2.5, 5)
        point = (2.5, 0)  # On the edge of the triangle
        self.assertTrue(is_point_inside_triangle(point[0], point[1], *triangle_vertices))

    def test_point_outside_triangle(self):
        """Test case where point is outside the triangle."""
        triangle_vertices = (0, 0, 5, 0, 2.5, 5)
        point = (6, 2)  # Outside the triangle
        self.assertFalse(is_point_inside_triangle(point[0], point[1], *triangle_vertices))

    def test_point_at_vertex(self):
        """Test case where point is at one of the triangle's vertices."""
        triangle_vertices = (0, 0, 5, 0, 2.5, 5)
        point = (0, 0)  # At the vertex of the triangle
        self.assertTrue(is_point_inside_triangle(point[0], point[1], *triangle_vertices))
if __name__ == '__main__':
    unittest.main()