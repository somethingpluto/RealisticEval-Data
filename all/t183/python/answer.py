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

def intersects(ray, circle):
    # Calculate the coefficients for the quadratic equation
    dx = ray.direction.x
    dy = ray.direction.y
    cx = circle.center.x
    cy = circle.center.y
    px = ray.origin.x
    py = ray.origin.y

    a = dx * dx + dy * dy
    b = 2 * (dx * (px - cx) + dy * (py - cy))
    c = (px - cx) * (px - cx) + (py - cy) * (py - cy) - circle.radius * circle.radius

    # Calculate the discriminant
    discriminant = b * b - 4 * a * c

    # No intersection if discriminant is negative
    if discriminant < 0:
        return False

    # Calculate the two possible intersection points (t values)
    sqrt_discriminant = math.sqrt(discriminant)
    t1 = (-b - sqrt_discriminant) / (2 * a)
    t2 = (-b + sqrt_discriminant) / (2 * a)

    # Check if either intersection point is on the ray (t >= 0)
    return t1 >= 0 or t2 >= 0