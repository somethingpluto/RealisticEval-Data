import math

def is_point_inside_triangle(px: float, py: float, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float) -> bool:
    def sign(p1x, p1y, p2x, p2y, p3x, p3y):
        return (p1x - p3x) * (p2y - p3y) - (p2x - p3x) * (p1y - p3y)
    
    d1 = sign(px, py, x1, y1, x2, y2)
    d2 = sign(px, py, x2, y2, x3, y3)
    d3 = sign(px, py, x3, y3, x1, y1)
    
    has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
    has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)
    
    return not (has_neg and has_pos)
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