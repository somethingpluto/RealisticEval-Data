describe('calculateBearing', () => {
    it('should calculate the bearing correctly', () => {
        const lat1 = 48.8566; // Paris, France
        const lon1 = 2.3522;
        const lat2 = 51.5074; // London, UK
        const lon2 = -0.1278;

        const expectedBearing = 90.0; // Approximate bearing from Paris to London

        const result = calculateBearing(lat1, lon1, lat2, lon2);

        expect(result).toBeCloseTo(expectedBearing, 2); // Allowing for a small margin of error
    });

    it('should handle edge cases', () => {
        const lat1 = 0; // North Pole
        const lon1 = 0;
        const lat2 = 0; // North Pole
        const lon2 = 180; // South Pole

        const expectedBearing = 180.0; // Bearing from North Pole to South Pole

        const result = calculateBearing(lat1, lon1, lat2, lon2);

        expect(result).toBeCloseTo(expectedBearing, 2);
    });
});