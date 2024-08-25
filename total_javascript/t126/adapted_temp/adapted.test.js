describe('calculateDistance', () => {
    test('calculates distance between two points in the same city', () => {
        // Coordinates for two points in Los Angeles
        const distance = calculateDistance(34.052235, -118.243683, 34.052236, -118.243684);
        expect(distance).toBeCloseTo(0.00014, 5);  // The distance should be very small
    });

    test('calculates distance between two major cities', () => {
        // Coordinates for Los Angeles and New York
        const distance = calculateDistance(34.052235, -118.243683, 40.712776, -74.005974);
        expect(distance).toBeCloseTo(3935.7, 1);  // Known distance is approximately 3940 kilometers
    });

    test('calculates distance between two points in different continents', () => {
        // Coordinates for New York in the USA and London in the UK
        const distance = calculateDistance(40.712776, -74.005974, 51.507351, -0.127758);
        expect(distance).toBeCloseTo(5570, 0);  // Known distance is approximately 5567 kilometers
    });

    test('handles zero distance when the same coordinates are given', () => {
        // Same coordinates for a location in Paris
        const distance = calculateDistance(48.8566, 2.3522, 48.8566, 2.3522);
        expect(distance).toBe(0);  // Distance should be zero
    });

    test('calculates correct distance with negative and positive longitude and latitude', () => {
        // Coordinates for Sydney and Auckland
        const distance = calculateDistance(-33.8688, 151.2093, -36.8485, 174.7633);
        expect(distance).toBeCloseTo(2156, 0);  // Known distance is approximately 2159 kilometers
    });
});
/**
 * Calculates the great-circle distance between two points on the Earth
 * using their latitude and longitude based on the Haversine formula.
 *
 * @param {number} lat1 - Latitude of the first point in degrees.
 * @param {number} lon1 - Longitude of the first point in degrees.
 * @param {number} lat2 - Latitude of the second point in degrees.
 * @param {number} lon2 - Longitude of the second point in degrees.
 * @returns {number} The distance between the two points in kilometers.
 */
function calculateDistance(lat1, lon1, lat2, lon2) {
    const earthRadiusKm = 6371; // Radius of the Earth in kilometers

    // Helper function to convert degrees to radians
    const toRadians = (degrees) => (Math.PI * degrees) / 180;

    // Convert all degrees to radians
    const lat1Rad = toRadians(lat1);
    const lon1Rad = toRadians(lon1);
    const lat2Rad = toRadians(lat2);
    const lon2Rad = toRadians(lon2);

    // Differences in coordinates
    const deltaLat = lat2Rad - lat1Rad;
    const deltaLon = lon2Rad - lon1Rad;

    // Haversine formula
    const a = Math.sin(deltaLat / 2) ** 2 +
              Math.cos(lat1Rad) * Math.cos(lat2Rad) *
              Math.sin(deltaLon / 2) ** 2;

    const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));

    // Distance in kilometers
    return earthRadiusKm * c;
}