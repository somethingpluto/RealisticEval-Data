/**
 * Given a set of points and a query point, write an algorithm to find the K nearest neighbors to the query point. The algorithm should efficiently handle large datasets, and the output should include the coordinates or indices of these neighbors.
 *
 * @param points Array of points from which to find the nearest neighbors.
 * @param queryPoint The point to which the nearest neighbors are found.
 * @param k The number of nearest neighbors to find.
 * @return An array containing the k nearest neighbors.
 */
class Point {
    double x, y;

    public Point(double x, double y) {
        this.x = x;
        this.y = y;
    }

    public double distanceTo(Point other) {
        return Math.sqrt(Math.pow(this.x - other.x, 2) + Math.pow(this.y - other.y, 2));
    }
}
public Point[] findKNearestNeighbors(Point[] points, Point queryPoint, int k) {}