package org.real.temp;

import static org.junit.Assert.assertEquals; 
import org.junit.Test;
import static org.real.temp.Answer.*;
public class Tester {

    private static final double DELTA = 1e-6; // Tolerance for floating-point comparisons

    @Test
    public void testSamePoint() {
        double lat = 52.2296756;
        double lon = 21.0122287;
        double result = haversineDistance(lat, lon, lat, lon);
        assertEquals(0.0, result, DELTA);
    }

    @Test
    public void testSmallDistance() {
        double lat1 = 52.2296756;
        double lon1 = 21.0122287;  // Warsaw, Poland
        double lat2 = 52.2296756;
        double lon2 = 21.0122297;  // Very close to the previous point
        double result = haversineDistance(lat1, lon1, lat2, lon2);
        assertEquals(0.0001, result, 1e-4);  // Expected small distance
    }

    @Test
    public void testLargeDistance() {
        double lat1 = 52.2296756;
        double lon1 = 21.0122287;  // Warsaw, Poland
        double lat2 = 41.8919300;
        double lon2 = 12.5113300;  // Rome, Italy
        double result = haversineDistance(lat1, lon1, lat2, lon2);
        assertEquals(1315.514, result, 1e-2);  // Approx distance in km
    }

    @Test
    public void testEquatorDistance() {
        double lat1 = 0.0;
        double lon1 = 0.0;  // Gulf of Guinea (Equator and Prime Meridian intersection)
        double lat2 = 0.0;
        double lon2 = 90.0;  // On the Equator, 90 degrees east
        double result = haversineDistance(lat1, lon1, lat2, lon2);
        assertEquals(10007.54, result, 1e-2);  // Approx quarter of Earth's circumference
    }

    @Test
    public void testPoleToPole() {
        double lat1 = 90.0;
        double lon1 = 0.0;  // North Pole
        double lat2 = -90.0;
        double lon2 = 0.0;  // South Pole
        double result = haversineDistance(lat1, lon1, lat2, lon2);
        assertEquals(20015.09, result, 1e-2);  // Approx half of Earth's circumference
    }
}
