package org.real.temp;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

public class Tester {

    // Helper method for comparing floating-point numbers with a tolerance
    private boolean approximatelyEqual(double a, double b, double epsilon) {
        return Math.abs(a - b) < epsilon;
    }

    @Test
    public void testNorthBearing() {
        // From equator directly north
        assertEquals(0, calculateBearing(0, 0, 10, 0), 1e-9);
    }

    @Test
    public void testEastBearing() {
        // From prime meridian directly east
        assertEquals(90, calculateBearing(0, 0, 0, 10), 1e-9);
    }

    @Test
    public void testSouthBearing() {
        // From a point directly south
        assertEquals(180, calculateBearing(10, 0, 0, 0), 1e-9);
    }

    @Test
    public void testWestBearing() {
        // From a point directly west
        assertEquals(270, calculateBearing(0, 10, 0, 0), 1e-9);
    }

    @Test
    public void testAcrossPrimeMeridian() {
        // From a point west of the prime meridian to a point east
        assertEquals(90, calculateBearing(0, -1, 0, 1), 1e-9);
    }
}
