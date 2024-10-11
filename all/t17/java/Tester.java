package org.real.temp;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class Tester {

    @Test
    void testSamePoint() {
        // Same point should return a distance of 0
        double lat = 52.2296756;
        double lon = 21.0122287;
        double result = haversine_distance(lat, lon, lat, lon);
        assertEquals(0.0, result, 1e-6); // Tolerance for floating point comparison
    }

    @Test
    void testSmallDistance() {
        // Points that are very close together (few meters apart)
        double lat1 = 52.2296756, lon1 = 21.0122287; // Warsaw, Poland
        double lat2 = 52.2296756, lon2 = 21.0122297; // Very close to the previous point
        double result = haversine_distance(lat1, lon1, lat2, lon2);
        assertEquals(0.0001, result, 1e-4); // Expected small distance
    }

    @Test
    void testLargeDistance() {
        // Points that are far apart
        double lat1 = 52.2296756, lon1 = 21.0122287; // Warsaw, Poland
        double lat2 = 41.8919300, lon2 = 12.5113300; // Rome, Italy
        double result = haversine_distance(lat1, lon1, lat2, lon2);
        assertEquals(1315.514, result, 1e-2); // Approx distance in km
    }

    @Test
    void testEquatorDistance() {
        // Points on the equator
        double lat1 = 0.0, lon1 = 0.0; // Gulf of Guinea (Equator and Prime Meridian intersection)
        double lat2 = 0.0, lon2 = 90.0; // On the Equator, 90 degrees east
        double result = haversine_distance(lat1, lon1, lat2, lon2);
        assertEquals(10007.54, result, 1e-2); // Approx quarter of Earth's circumference
    }

    @Test
    void testPoleToPole() {
        // Distance from North Pole to South Pole
        double lat1 = 90.0, lon1 = 0.0; // North Pole
        double lat2 = -90.0, lon2 = 0.0; // South Pole
        double result = haversine_distance(lat1, lon1, lat2, lon2);
        assertEquals(20015.09, result, 1e-2); // Approx half of Earth's circumference
    }
}
