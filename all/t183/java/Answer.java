package org.real.temp;

public class Answer {

    static class Point {
        float x, y;

        Point(float x, float y) {
            this.x = x;
            this.y = y;
        }
    }

    static class Ray {
        Point origin;   // Starting point of the ray
        Point direction; // Direction of the ray (should be normalized)

        Ray(Point origin, Point direction) {
            this.origin = origin;
            this.direction = direction;
        }
    }

    static class Circle {
        Point center; // Center of the circle
        float radius; // Radius of the circle

        Circle(Point center, float radius) {
            this.center = center;
            this.radius = radius;
        }
    }

    // Method to check if the ray intersects the circle
    public static boolean intersects(Ray ray, Circle circle) {
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
        float sqrtDiscriminant = (float) Math.sqrt(discriminant);
        float t1 = (-b - sqrtDiscriminant) / (2 * a);
        float t2 = (-b + sqrtDiscriminant) / (2 * a);

        // Check if either intersection point is on the ray (t >= 0)
        return (t1 >= 0 || t2 >= 0);
    }
}