/**
 * Determines if the point (x, y) is inside the given polygon.
 * The polygon is defined as a list of tuples (x, y) representing the vertices.
 *
 * @param point  A tuple (x, y) representing the point to check.
 * @param polygon A list of tuples (x, y) representing the vertices of the polygon.
 * @return True if the point is inside the polygon, False otherwise.
 */
static class Point {
    double x;
    double y;

    Point(double x, double y) {
        this.x = x;
        this.y = y;
    }
}
public static boolean isPointInPolygon(Point point, List<Point> polygon) {}