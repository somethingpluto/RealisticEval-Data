/**
 * Calculates the intersection point of two line segments, if it exists.
 *
 * @param seg1 Coordinates of the first line segment, defined as ((x1, y1), (x2, y2)).
 * @param seg2 Coordinates of the second line segment, defined as ((x3, y3), (x4, y4)).
 * @return A Point representing the (x, y) coordinates of the intersection point if the line segments intersect,
 *         otherwise null.
 */
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
public static Point getLineSegmentIntersection(Point seg1Start, Point seg1End, Point seg2Start, Point seg2End) {}