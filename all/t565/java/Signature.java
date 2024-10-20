/**
 * Recursively calculates a point on a Bézier curve using De Casteljau's algorithm.
 *
 * @param t - A value between 0 and 1 representing the interpolation parameter.
 * @param points - An array of control points defining the Bézier curve.
 * @return The calculated Coordinates at the given parameter t.
 */
static class Coordinates {
    double x;
    double y;

    Coordinates(double x, double y) {
        this.x = x;
        this.y = y;
    }
}
public static Coordinates getBezierPoint(double t, Coordinates[] points) {}