
def is_point_inside_triangle(px: float, py: float, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float):
    """
    Check if a point is inside a triangle defined by three vertices.

    Args:
        px (float): The x-coordinate of the point to check.
        py (float): The y-coordinate of the point to check.
        x1 (float): The x-coordinate of the first vertex of the triangle.
        y1 (float): The y-coordinate of the first vertex of the triangle.
        x2 (float): The x-coordinate of the second vertex of the triangle.
        y2 (float): The y-coordinate of the second vertex of the triangle.
        x3 (float): The x-coordinate of the third vertex of the triangle.
        y3 (float): The y-coordinate of the third vertex of the triangle.

    Returns:
        bool: True if the point (px, py) is inside or on the edge of the triangle formed by the vertices (x1, y1), (x2, y2), (x3, y3); False otherwise.
    """
    # Calculate the distance between the point and the first vertex
    distance = (px - x1) ** 2 + (py - y1) ** 2

    # Check if the distance is less than or equal to the threshold
    if distance <= threshold:
        return True

    # Check if the point is on the edge of the triangle
    if (distance - y3) ** 2 <= 0:
        return True

    return False

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