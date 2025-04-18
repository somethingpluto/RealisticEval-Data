package org.real.temp;

public class Answer {

    /**
     * Calculate the area of a triangle given by its vertices.
     * @param x1 x-coordinate of vertex 1
     * @param y1 y-coordinate of vertex 1
     * @param x2 x-coordinate of vertex 2
     * @param y2 y-coordinate of vertex 2
     * @param x3 x-coordinate of vertex 3
     * @param y3 y-coordinate of vertex 3
     * @return the area of the triangle
     */
    public static double calculateTriangleArea(double x1, double y1, double x2, double y2, double x3, double y3) {
        return Math.abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0);
    }

    /**
     * Check if a point (px, py) is inside the triangle formed by (x1, y1), (x2, y2), (x3, y3).
     * @param px x-coordinate of the point
     * @param py y-coordinate of the point
     * @param x1 x-coordinate of vertex 1
     * @param y1 y-coordinate of vertex 1
     * @param x2 x-coordinate of vertex 2
     * @param y2 y-coordinate of vertex 2
     * @param x3 x-coordinate of vertex 3
     * @param y3 y-coordinate of vertex 3
     * @return true if the point is inside the triangle, false otherwise
     */
    public static boolean isPointInsideTriangle(double px, double py, double x1, double y1, double x2, double y2, double x3, double y3) {
        // Calculate the area of the triangle ABC
        double A = calculateTriangleArea(x1, y1, x2, y2, x3, y3);

        // Calculate the area of the triangle PAB, PBC, and PCA
        double A1 = calculateTriangleArea(px, py, x1, y1, x2, y2);
        double A2 = calculateTriangleArea(px, py, x2, y2, x3, y3);
        double A3 = calculateTriangleArea(px, py, x3, y3, x1, y1);

        // Check if the sum of A1, A2, and A3 is equal to A
        return Math.abs(A - (A1 + A2 + A3)) < 1e-9; // Using a small epsilon for floating-point comparison
    }
}