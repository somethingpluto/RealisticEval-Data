#include <iostream>
#include <cmath>

struct Point {
    float x, y;
};

struct Ray {
    Point origin;   // Starting point of the ray
    Point direction; // Direction of the ray (should be normalized)
};

struct Circle {
    Point center; // Center of the circle
    float radius; // Radius of the circle
};

// Function to check if the ray intersects the circle
bool intersects(const Ray& ray, const Circle& circle) {
    // Calculate the coefficients for the quadratic equation
    float dx = ray.direction.x;
    float dy = ray.direction.y;
    float cx = circle.center.x;
    float cy = circle.center.y;
    float px = ray.origin.x;
    float py = ray.origin.y;

    float a = dx * dx + dy * dy;
    float b = 2 * (dx * (px - cx) + dy * (py - cy));
    float c = (px - cx) * (px - cx) + (py - cy) * (py - cy) - circle.radius * circle.radius;

    // Calculate the discriminant
    float discriminant = b * b - 4 * a * c;

    // No intersection if discriminant is negative
    if (discriminant < 0) {
        return false;
    }

    // Calculate the two possible intersection points (t values)
    float sqrtDiscriminant = std::sqrt(discriminant);
    float t1 = (-b - sqrtDiscriminant) / (2 * a);
    float t2 = (-b + sqrtDiscriminant) / (2 * a);

    // Check if either intersection point is on the ray (t >= 0)
    return (t1 >= 0 || t2 >= 0);
}