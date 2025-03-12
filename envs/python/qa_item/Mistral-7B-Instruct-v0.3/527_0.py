def is_point_inside_triangle(px, py, x1, y1, x2, y2, x3, y3):
    area = 0.5 * abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1))

    d1 = ((x2 - x1) * (py - y1) - (y2 - y1) * (px - x1))
    d2 = ((x3 - x1) * (py - y1) - (y3 - y1) * (px - x1))

    return (d1 >= 0 and d1 <= area) or (d2 >= 0 and d2 <= area)
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