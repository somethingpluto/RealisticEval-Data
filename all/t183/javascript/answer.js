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