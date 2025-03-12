import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Ray:
    def __init__(self, origin, direction):
        self.origin = origin  # Starting point of the ray
        self.direction = direction  # Direction of the ray (should be normalized)

class Circle:
    def __init__(self, center, radius):
        self.center = center  # Center of the circle
        self.radius = radius  # Radius of the circle

def intersects(ray: Ray, circle: Circle) -> bool:
    """
    Determines whether a ray intersects with a circle.

    Args:
        ray (Ray): The ray to be tested for intersection. It is assumed to contain properties such as an origin point (x, y) and a direction vector (dx, dy).
        circle (Circle): The circle to check for intersection. It is assumed to contain properties such as a center point (h, k) and a radius r.

    Returns:
        bool: True if the ray intersects the circle; False otherwise.
    """
    ox, oy = ray.origin.x, ray.origin.y
    dx, dy = ray.direction.x, ray.direction.y
    h, k = circle.center.x, circle.center.y
    r = circle.radius

    a = dx**2 + dy**2
    b = 2 * (dx * (ox - h) + dy * (oy - k))
    c = (ox - h)**2 + (oy - k)**2 - r**2

    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        return False
    else:
        return True
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Ray:
    def __init__(self, origin, direction):
        self.origin = origin  # Starting point of the ray
        self.direction = direction  # Direction of the ray (should be normalized)


class Circle:
    def __init__(self, center, radius):
        self.center = center  # Center of the circle
        self.radius = radius  # Radius of the circleimport unittest


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Ray:
    def __init__(self, origin, direction):
        self.origin = origin  # Starting point of the ray
        self.direction = direction  # Direction of the ray (should be normalized)


class Circle:
    def __init__(self, center, radius):
        self.center = center  # Center of the circle
        self.radius = radius  # Radius of the circle


class Tester(unittest.TestCase):
    def test_ray_circle_intersection(self):
        # Test Case 1: The ray intersects the circle at two points
        ray = Ray(Point(0, 0), Point(1, 1))  # Origin at (0, 0), direction (1, 1)
        circle = Circle(Point(3, 3), 2)  # Circle center at (3, 3), radius 2
        self.assertTrue(intersects(ray, circle))

        # Test Case 2: The ray is tangent to the circle (one intersection point)
        ray = Ray(Point(2, 0), Point(0, 1))  # Origin at (2, 0), direction (0, 1)
        circle = Circle(Point(2, 2), 1)  # Circle center at (2, 2), radius 1
        self.assertTrue(intersects(ray, circle))

        # Test Case 3: The ray starts inside the circle (one intersection point)
        ray = Ray(Point(2, 2), Point(1, 0))  # Origin at (2, 2), direction (1, 0)
        circle = Circle(Point(3, 2), 1)  # Circle center at (3, 2), radius 1
        self.assertTrue(intersects(ray, circle))

        # Test Case 4: The ray originates outside and goes away from the circle (no intersection)
        ray = Ray(Point(5, 5), Point(1, 0))  # Origin at (5, 5), direction (1, 0)
        circle = Circle(Point(3, 3), 1)  # Circle center at (3, 3), radius 1
        self.assertFalse(intersects(ray, circle))

        # Test Case 5: The ray is parallel to the line connecting the center of the circle and is outside (no intersection)
        ray = Ray(Point(0, 3), Point(1, 0))  # Origin at (0, 3), direction (1, 0)
        circle = Circle(Point(3, 3), 1)  # Circle center at (3, 3), radius 1
        self.assertFalse(intersects(ray, circle))

        # Test Case 6: The ray intersects the circle at one point when passing through the center
        ray = Ray(Point(3, 0), Point(0, 1))  # Origin at (3, 0), direction (0, 1)
        circle = Circle(Point(3, 3), 3)  # Circle center at (3, 3), radius 3
        self.assertTrue(intersects(ray, circle))

if __name__ == '__main__':
    unittest.main()