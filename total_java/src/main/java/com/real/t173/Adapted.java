package com.real.t173;

public class Adapted {
    /**
     * Calculate the coordinates of a cubic Bézier curve at a given parametert(typically between 0 and 1).
     * @param t
     * @param p0
     * @param p1
     * @param p2
     * @param p3
     * @return
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
