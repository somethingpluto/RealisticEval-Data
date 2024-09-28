def area(x1, y1, x2, y2, x3, y3):
    """Calculate the area of a triangle given by its vertices."""
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)


def is_point_inside_triangle(px, py, x1, y1, x2, y2, x3, y3):
    """Check if a point (px, py) is inside the triangle formed by (x1, y1), (x2, y2), (x3, y3)."""
    # Calculate the area of the triangle ABC
    A = area(x1, y1, x2, y2, x3, y3)

    # Calculate the area of the triangle PAB, PBC, and PCA
    A1 = area(px, py, x1, y1, x2, y2)
    A2 = area(px, py, x2, y2, x3, y3)
    A3 = area(px, py, x3, y3, x1, y1)

    # Check if the sum of A1, A2, and A3 is equal to A
    return A == A1 + A2 + A3
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