package com.real.t174;

public class Adapted {
    // Bézier curve definition, assuming quadratic for simplicity
    public static double bezierCurve(double t, double p0, double p1, double p2) {
        double oneMinusT = 1 - t;
        return oneMinusT * oneMinusT * p0 + 2 * oneMinusT * t * p1 + t * t * p2;
    }

    // Secant method to find the t value where Bézier curve reaches the target x value
    public static double findTForX(double targetX, double p0, double p1, double p2) {
        double t0 = 0.0;
        double t1 = 1.0;
        double tolerance = 1e-6;
        int maxIterations = 100;

        double x0 = bezierCurve(t0, p0, p1, p2) - targetX;
        double x1 = bezierCurve(t1, p0, p1, p2) - targetX;

        for (int i = 0; i < maxIterations; i++) {
            if (Math.abs(x1 - x0) < tolerance) {
                break;
            }

            double t2 = t1 - x1 * (t1 - t0) / (x1 - x0);
            double x2 = bezierCurve(t2, p0, p1, p2) - targetX;

            if (Math.abs(x2) < tolerance) {
                return t2;
            }

            t0 = t1;
            x0 = x1;
            t1 = t2;
            x1 = x2;
        }

        return t1; // Return the best approximation found
    }

}
