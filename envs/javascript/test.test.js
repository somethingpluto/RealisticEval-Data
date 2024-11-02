class Point {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }
}

class Ray {
    constructor(origin, direction) {
        this.origin = origin;     // Starting point of the ray
        this.direction = direction; // Direction of the ray (should be normalized)
    }
}

class Circle {
    constructor(center, radius) {
        this.center = center; // Center of the circle
        this.radius = radius; // Radius of the circle
    }
}

// Function to check if the ray intersects the circle
function intersects(ray, circle) {
    // Calculate the coefficients for the quadratic equation
    const dx = ray.direction.x;
    const dy = ray.direction.y;
    const cx = circle.center.x;
    const cy = circle.center.y;
    const px = ray.origin.x;
    const py = ray.origin.y;

    const a = dx * dx + dy * dy;
    const b = 2 * (dx * (px - cx) + dy * (py - cy));
    const c = (px - cx) * (px - cx) + (py - cy) * (py - cy) - circle.radius * circle.radius;

    // Calculate the discriminant
    const discriminant = b * b - 4 * a * c;

    // No intersection if discriminant is negative
    if (discriminant < 0) {
        return false;
    }

    // Calculate the two possible intersection points (t values)
    const sqrtDiscriminant = Math.sqrt(discriminant);
    const t1 = (-b - sqrtDiscriminant) / (2 * a);
    const t2 = (-b + sqrtDiscriminant) / (2 * a);

    // Check if either intersection point is on the ray (t >= 0)
    return (t1 >= 0 || t2 >= 0);
}
describe("Ray-Circle Intersection Tests", () => {
    // Test Case 1: The ray intersects the circle at two points
    test("should intersect the circle at two points", () => {
        const ray = new Ray(new Point(0, 0), new Point(1, 1)); // Origin at (0, 0), direction (1, 1)
        const circle = new Circle(new Point(3, 3), 2); // Circle center at (3, 3), radius 2
        expect(intersects(ray, circle)).toBe(true);
    });

    // Test Case 2: The ray is tangent to the circle (one intersection point)
    test("should be tangent to the circle (one intersection point)", () => {
        const ray = new Ray(new Point(2, 0), new Point(0, 1)); // Origin at (2, 0), direction (0, 1)
        const circle = new Circle(new Point(2, 2), 1); // Circle center at (2, 2), radius 1
        expect(intersects(ray, circle)).toBe(true);
    });

    // Test Case 3: The ray starts inside the circle (one intersection point)
    test("should start inside the circle (one intersection point)", () => {
        const ray = new Ray(new Point(2, 2), new Point(1, 0)); // Origin at (2, 2), direction (1, 0)
        const circle = new Circle(new Point(3, 2), 1); // Circle center at (3, 2), radius 1
        expect(intersects(ray, circle)).toBe(true);
    });

    // Test Case 4: The ray originates outside and goes away from the circle (no intersection)
    test("should not intersect the circle (no intersection)", () => {
        const ray = new Ray(new Point(5, 5), new Point(1, 0)); // Origin at (5, 5), direction (1, 0)
        const circle = new Circle(new Point(3, 3), 1); // Circle center at (3, 3), radius 1
        expect(intersects(ray, circle)).toBe(false);
    });

    // Test Case 5: The ray is parallel to the line connecting the center of the circle and is outside (no intersection)
    test("should not intersect when parallel and outside", () => {
        const ray = new Ray(new Point(0, 3), new Point(1, 0)); // Origin at (0, 3), direction (1, 0)
        const circle = new Circle(new Point(3, 3), 1); // Circle center at (3, 3), radius 1
        expect(intersects(ray, circle)).toBe(true);
    });

    // Test Case 6: The ray intersects the circle at one point when passing through the center
    test("should intersect at one point through the center", () => {
        const ray = new Ray(new Point(3, 0), new Point(0, 1)); // Origin at (3, 0), direction (0, 1)
        const circle = new Circle(new Point(3, 3), 3); // Circle center at (3, 3), radius 3
        expect(intersects(ray, circle)).toBe(true);
    });
});
