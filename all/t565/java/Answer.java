import java.awt.Point;

public class BezierCurve {

    // Define a Coordinates class to represent a point in 2D space
    static class Coordinates {
        double x;
        double y;

        Coordinates(double x, double y) {
            this.x = x;
            this.y = y;
        }
    }

    /**
     * Recursively calculates a point on a Bézier curve using De Casteljau's algorithm.
     *
     * @param t      A value between 0 and 1 representing the interpolation parameter.
     * @param points An array of control points defining the Bézier curve.
     * @return The calculated Coordinates at the given parameter t.
     */
    public static Coordinates getBezierPoint(double t, Coordinates[] points) {
        // If there's only one point, return it as the result
        if (points.length == 1) {
            return points[0];
        }

        // Create an array to hold the points for the next iteration
        Coordinates[] nextPoints = new Coordinates[points.length - 1];

        // Calculate the intermediate points for the next iteration
        for (int i = 0; i < points.length - 1; i++) {
            double x = (1 - t) * points[i].x + t * points[i + 1].x;
            double y = (1 - t) * points[i].y + t * points[i + 1].y;
            nextPoints[i] = new Coordinates(x, y);
        }

        // Recursively call getBezierPoint with the new points
        return getBezierPoint(t, nextPoints);
    }
}