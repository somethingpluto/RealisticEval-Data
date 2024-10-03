package org.real.temp;

public class Answer {
    /**
     * Calculate the coordinates of a cubic Bézier curve at a given parametert(typically between 0 and 1).
     * @param t  A double representing the parameter along the curve, where 0 <= t <= 1.
     * @param p0 A double array of size 2 representing the x and y coordinates of the start point.
     * @param p1 A double array of size 2 representing the x and y coordinates of the first control point.
     * @param p2 A double array of size 2 representing the x and y coordinates of the second control point.
     * @param p3 A double array of size 2 representing the x and y coordinates of the end point.
     * @return   A double array of size 2 containing the x and y coordinates of the point on the curve corresponding to the parameter t.
     */
    public static double[] cubicBezier(double t, double[] p0, double[] p1, double[] p2, double[] p3) {
        double x = Math.pow(1 - t, 3) * p0[0]
                + 3 * Math.pow(1 - t, 2) * t * p1[0]
                + 3 * (1 - t) * Math.pow(t, 2) * p2[0]
                + Math.pow(t, 3) * p3[0];

        double y = Math.pow(1 - t, 3) * p0[1]
                + 3 * Math.pow(1 - t, 2) * t * p1[1]
                + 3 * (1 - t) * Math.pow(t, 2) * p2[1]
                + Math.pow(t, 3) * p3[1];

        return new double[]{x, y};
    }
}
