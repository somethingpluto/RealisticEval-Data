package org.real.temp;

/**
 * Represents a point in 2D space.
 */
class Point {
    float x, y;

    Point(float x, float y) {
        this.x = x;
        this.y = y;
    }
}

/**
 * Represents a ray in 2D space.
 * The ray is defined by its origin and direction (which should be normalized).
 */
class Ray {
    Point origin;   // Starting point of the ray
    Point direction; // Direction of the ray (should be normalized)

    Ray(Point origin, Point direction) {
        this.origin = origin;
        this.direction = direction;
    }
}

/**
 * Represents a circle in 2D space.
 * The circle is defined by its center and radius.
 */
class Circle {
    Point center; // Center of the circle
    float radius; // Radius of the circle

    Circle(Point center, float radius) {
        this.center = center;
        this.radius = radius;
    }
}