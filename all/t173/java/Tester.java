package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertArrayEquals;

import org.real.temp.*;
public class Tester {

    @Test
    public void testCubicBezier_t0() {
        double[] p0 = {0.0, 0.0};
        double[] p1 = {0.0, 1.0};
        double[] p2 = {1.0, 1.0};
        double[] p3 = {1.0, 0.0};

        double t = 0.0;
        double[] expected = {0.0, 0.0};
        assertArrayEquals(expected, Answer.cubicBezier(t, p0, p1, p2, p3));
    }

    @Test
    public void testCubicBezier_t1() {
        double[] p0 = {0.0, 0.0};
        double[] p1 = {0.0, 1.0};
        double[] p2 = {1.0, 1.0};
        double[] p3 = {1.0, 0.0};

        double t = 1.0;
        double[] expected = {1.0, 0.0};
        assertArrayEquals(expected, Answer.cubicBezier(t, p0, p1, p2, p3));
    }

    @Test
    public void testCubicBezier_t0_5() {
        double[] p0 = {0.0, 0.0};
        double[] p1 = {0.0, 1.0};
        double[] p2 = {1.0, 1.0};
        double[] p3 = {1.0, 0.0};

        double t = 0.5;
        double[] expected = {0.5, 0.75};
        assertArrayEquals(expected, Answer.cubicBezier(t, p0, p1, p2, p3), 1e-9);
    }

    @Test
    public void testCubicBezier_midPoint() {
        double[] p0 = {0.0, 0.0};
        double[] p1 = {1.0, 1.0};
        double[] p2 = {2.0, 1.0};
        double[] p3 = {3.0, 0.0};

        double t = 0.5;
        double[] expected = {1.5, 0.75};
        assertArrayEquals(expected, Answer.cubicBezier(t, p0, p1, p2, p3), 1e-9);
    }

    @Test
    public void testCubicBezier_arbitraryT() {
        double[] p0 = {0.0, 0.0};
        double[] p1 = {0.0, 2.0};
        double[] p2 = {2.0, 2.0};
        double[] p3 = {2.0, 0.0};
        double t = 0.75;
        double[] expected = {1.6875, 1.125};
        assertArrayEquals(expected, Answer.cubicBezier(t, p0, p1, p2, p3), 1e-9);
    }

}
