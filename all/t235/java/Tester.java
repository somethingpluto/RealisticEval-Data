package org.real.temp;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class Tester {

    @Test
    public void testCalculateBearing() {
        double lat1 = 51.5074;
        double lon1 = -0.1278;
        double lat2 = 40.7128;
        double lon2 = -74.0060;

        double expectedBearing = 99.1; // Example expected bearing, adjust as necessary

        double actualBearing = GeoUtils.calculateBearing(lat1, lon1, lat2, lon2);

        assertEquals(expectedBearing, actualBearing, "The calculated bearing should match the expected value");
    }
}