def is_point_inside_triangle(px: float, py: float, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float) -> bool:
    # Calculate area of triangle ABC
    area_ABC = abs(((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2.0))

    # Calculate area of triangle PBC, PAB, and PCA
    area_PBC = abs(((px*(y2 - y3) + x2*(py - y3) + x3*(y3 - py) ) / 2.0))
    area_PAB = abs(((x1*(py - y3) + px*(y3 - y1) + x3*(y1 - py) ) / 2.0))
    area_PCA = abs(((x1*(y2 - py) + x2*(py - y1) + px*(y1 - y2) ) / 2.0))

    # If sum of areas equals to area of ABC, then point is inside triangle
    return area_ABC == (area_PBC + area_PAB + area_PCA)
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