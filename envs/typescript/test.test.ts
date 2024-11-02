interface Point {
    x: number;
    y: number;
}

interface Ray {
    origin: Point;     // Starting point of the ray
    direction: Point;  // Direction of the ray (should be normalized)
}

interface Circle {
    center: Point;     // Center of the circle
    radius: number;    // Radius of the circle
}

// Function to check if the ray intersects the circle
function intersects(ray: Ray, circle: Circle): boolean {
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
describe('Ray-Circle Intersection Tests', () => {
    // Test Case 1: The ray intersects the circle at two points
    test('Ray intersects circle at two points', () => {
        const ray = { origin: { x: 0, y: 0 }, direction: { x: 1, y: 1 } };
        const circle = { center: { x: 3, y: 3 }, radius: 2 };
        expect(intersects(ray, circle)).toBe(true);
    });

    // Test Case 2: The ray is tangent to the circle (one intersection point)
    test('Ray is tangent to the circle', () => {
        const ray = { origin: { x: 2, y: 0 }, direction: { x: 0, y: 1 } };
        const circle = { center: { x: 2, y: 2 }, radius: 1 };
        expect(intersects(ray, circle)).toBe(true);
    });

    // Test Case 3: The ray starts inside the circle (one intersection point)
    test('Ray starts inside the circle', () => {
        const ray = { origin: { x: 2, y: 2 }, direction: { x: 1, y: 0 } };
        const circle = { center: { x: 3, y: 2 }, radius: 1 };
        expect(intersects(ray, circle)).toBe(true);
    });

    // Test Case 4: The ray originates outside and goes away from the circle (no intersection)
    test('Ray goes away from circle (no intersection)', () => {
        const ray = { origin: { x: 5, y: 5 }, direction: { x: 1, y: 0 } };
        const circle = { center: { x: 3, y: 3 }, radius: 1 };
        expect(intersects(ray, circle)).toBe(false);
    });

    // Test Case 5: The ray is parallel to the line connecting the center of the circle and is outside (no intersection)
    test('Ray is parallel and outside circle (no intersection)', () => {
        const ray = { origin: { x: 0, y: 3 }, direction: { x: 1, y: 0 } };
        const circle = { center: { x: 3, y: 3 }, radius: 1 };
        expect(intersects(ray, circle)).toBe(false);
    });

    // Test Case 6: The ray intersects the circle at one point when passing through the center
    test('Ray passes through center of circle', () => {
        const ray = { origin: { x: 3, y: 0 }, direction: { x: 0, y: 1 } };
        const circle = { center: { x: 3, y: 3 }, radius: 3 };
        expect(intersects(ray, circle)).toBe(true);
    });
});
