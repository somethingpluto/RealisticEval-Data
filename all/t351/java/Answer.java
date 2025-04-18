package org.real.temp;

public class Answer {
    public static double bezier(double t, double p0, double p1, double p2, double p3) {
        double d = 1 - t;
        return p0 * d * d * d + 3 * p1 * d * d * t + 3 * p2 * d * t * t + p3 * t * t * t;
    }
}
