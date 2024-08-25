describe('calculateDistance', () => {
    test('calculates distance between two points in the same city', () => {
        // Coordinates for two points in Los Angeles
        const distance = calculateDistance(34.052235, -118.243683, 34.052236, -118.243684);
        expect(distance).toBeCloseTo(0.00013, 5);  // The distance should be very small
    });

    test('calculates distance between two major cities', () => {
        // Coordinates for Los Angeles and New York
        const distance = calculateDistance(34.052235, -118.243683, 40.712776, -74.005974);
        expect(distance).toBeCloseTo(3940, 0);  // Known distance is approximately 3940 kilometers
    });

    test('calculates distance between two points in different continents', () => {
        // Coordinates for New York in the USA and London in the UK
        const distance = calculateDistance(40.712776, -74.005974, 51.507351, -0.127758);
        expect(distance).toBeCloseTo(5567, 0);  // Known distance is approximately 5567 kilometers
    });

    test('handles zero distance when the same coordinates are given', () => {
        // Same coordinates for a location in Paris
        const distance = calculateDistance(48.8566, 2.3522, 48.8566, 2.3522);
        expect(distance).toBe(0);  // Distance should be zero
    });

    test('calculates correct distance with negative and positive longitude and latitude', () => {
        // Coordinates for Sydney and Auckland
        const distance = calculateDistance(-33.8688, 151.2093, -36.8485, 174.7633);
        expect(distance).toBeCloseTo(2159, 0);  // Known distance is approximately 2159 kilometers
    });
});