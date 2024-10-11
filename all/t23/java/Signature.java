/**
 * Calculates the intersection point of two line segments, if it exists.
 *
 * @param seg1 Coordinates of the first line segment, defined as an array of four doubles [x1, y1, x2, y2].
 * @param seg2 Coordinates of the second line segment, defined as an array of four doubles [x3, y3, x4, y4].
 * @return A double array containing the (x, y) coordinates of the intersection point if the line segments intersect, otherwise null.
 */
public class LineSegmentIntersection {

    public static double[] getLineSegmentIntersection(double[] seg1, double[] seg2) {
        // Create Line2D objects for both segments
        Line2D.Double line1 = new Line2D.Double(seg1[0], seg1[1], seg1[2], seg1[3]);
        Line2D.Double line2 = new Line2D.Double(seg2[0], seg2[1], seg2[2], seg2[3]);

        // Check if the lines intersect
        if (line1.intersectsLine(line2)) {
            // Get the intersection point
            Point2D.Double intersectionPoint = new Point2D.Double();
            line1.intersectLine(line2, intersectionPoint);
            return new double[]{intersectionPoint.x, intersectionPoint.y};
        } else {
            return null;
        }
    }

    public static void main(String[] args) {
        // Example usage
        double[] seg1 = {0, 0, 1, 1};
        double[] seg2 = {1, 0, 0, 1};
        double[] intersection = getLineSegmentIntersection(seg1, seg2);

        if (intersection != null) {
            System.out.println("Intersection at: (" + intersection[0] + ", " + intersection[1] + ")");
        } else {
            System.out.println("No intersection");
        }
    }
}