#include <iostream>
#include <cmath>

// Function to calculate the area of a triangle given by its vertices
double area(double x1, double y1, double x2, double y2, double x3, double y3) {
    return std::abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0);
}

// Function to check if a point (px, py) is inside the triangle formed by (x1, y1), (x2, y2), (x3, y3)
bool is_point_inside_triangle(double px, double py, double x1, double y1, double x2, double y2, double x3, double y3) {
    // Calculate the area of the triangle ABC
    double A = area(x1, y1, x2, y2, x3, y3);

    // Calculate the area of the triangles PAB, PBC, and PCA
    double A1 = area(px, py, x1, y1, x2, y2);
    double A2 = area(px, py, x2, y2, x3, y3);
    double A3 = area(px, py, x3, y3, x1, y1);

    // Check if the sum of A1, A2, and A3 is equal to A
    return std::abs(A - (A1 + A2 + A3)) < 1e-9; // Using a small epsilon value for floating-point comparison
}