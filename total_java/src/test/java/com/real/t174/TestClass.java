package com.real.t174;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

// Import the correct class
import com.real.t174.Adapted;

public class TestClass {
    // Tolerance level for floating-point comparisons
    private static final double TOLERANCE = 1e-6;

    @Test
    public void testFindTForX_AtStart() {
        double p0 = 0.0;
        double p1 = 0.5;
        double p2 = 1.0;
        double targetX = 0.0;

        double t = Adapted.findTForX(targetX, p0, p1, p2);
        assertEquals(0.0, t, TOLERANCE);
    }

    @Test
    public void testFindTForX_AtEnd() {
        double p0 = 0.0;
        double p1 = 0.5;
        double p2 = 1.0;
        double targetX = 1.0;

        double t = Adapted.findTForX(targetX, p0, p1, p2);
        assertEquals(1.0, t, TOLERANCE);
    }

    @Test
    public void testFindTForX_MidCurve() {
        double p0 = 0.0;
        double p1 = 0.5;
        double p2 = 1.0;
        double targetX = 0.25;

        double t = Adapted.findTForX(targetX, p0, p1, p2);
        assertEquals(0.25, t, TOLERANCE);
    }


    @Test
    public void testFindTForX_NearMidCurve() {
        double p0 = 0.0;
        double p1 = 1.0;
        double p2 = 2.0;
        double targetX = 1.5;

        double t = Adapted.findTForX(targetX, p0, p1, p2);
        assertEquals(0.75, t, TOLERANCE);
    }

}
