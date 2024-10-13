package org.real.temp;

public class Answer {

    public static void main(String[] args) {
        // Example usage
        System.out.println(getLineSegmentIntersection(
                new Point(0, 0), new Point(5, 5),
                new Point(0, 5), new Point(5, 0)
        )); // Expected output: (2.5, 2.5)
    }

    public static Point getLineSegmentIntersection(Point p1, Point p2, Point p3, Point p4) {
        double x1 = p1.x, y1 = p1.y;
        double x2 = p2.x, y2 = p2.y;
        double x3 = p3.x, y3 = p3.y;
        double x4 = p4.x, y4 = p4.y;

        // Compute direction vectors and determinant
        double dx1 = x2 - x1, dy1 = y2 - y1;
        double dx2 = x4 - x3, dy2 = y4 - y3;
        double determinant = dx1 * dy2 - dx2 * dy1;

        // Check for parallel lines or identical segments
        if (Math.abs(determinant) < 1e-10) {
            return null;
        }

        // Calculate intersection parameters
        double t1 = ((x3 - x1) * dy2 - (y3 - y1) * dx2) / determinant;
        double t2 = ((x3 - x1) * dy1 - (y3 - y1) * dx1) / determinant;

        // Allow for a small tolerance in the intersection check
        double tolerance = 1e-10;

        // Check if intersection is within the bounds of the line segments
        if (0 - tolerance <= t1 && t1 <= 1 + tolerance && 0 - tolerance <= t2 && t2 <= 1 + tolerance) {
            double x = x1 + t1 * dx1;
            double y = y1 + t1 * dy1;
            return new Point(Math.round(x * 1e7) / 1e7, Math.round(y * 1e7) / 1e7);
        }

        return null;
    }

    static class Point {
        double x, y;

        Point(double x, double y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public String toString() {
            return "(" + x + ", " + y + ")";
        }
    }
}