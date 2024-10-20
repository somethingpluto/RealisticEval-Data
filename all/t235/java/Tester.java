package org.real.temp;


import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.*;
public class Tester {


    @Test
    public void testNorthBearing() {
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
