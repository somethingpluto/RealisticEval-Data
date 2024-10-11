package org.real.temp;

public class Answer {
    public static double[] getLineSegmentIntersection(double[][] seg1, double[][] seg2) {
        // Extract points from segments
        double x1 = seg1[0][0];
        double y1 = seg1[0][1];
        double x2 = seg1[1][0];
        double y2 = seg1[1][1];
        double x3 = seg2[0][0];
        double y3 = seg2[0][1];
        double x4 = seg2[1][0];
        double y4 = seg2[1][1];

        // Calculate denominator for intersection calculation
        double denominator = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1);
        // Check if denominator is zero, which means lines are parallel or collinear
        if (denominator == 0) {
            return null; // Lines do not intersect
        }

        // Calculate t and u values using Cramer's rule
        double t = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / denominator;
        double u = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / denominator;

        // Check if intersection point lies within both segments
        if (t >= 0 && t <= 1 && u >= 0 && u <= 1) {
            // Intersection point exists
            return new double[]{x1 + t * (x2 - x1), y1 + t * (y2 - y1)};
        } else {
            // Intersection point does not lie within both segments
            return null;
        }
    }
}
