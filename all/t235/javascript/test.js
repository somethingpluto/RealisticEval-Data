describe('calculateBearing', () => {
  it('should calculate the correct bearing between two points', () => {
    const lat1 = 48.8566; // Paris, France
    const lon1 = 2.3522;
    const lat2 = 51.5074; // London, UK
    const lon2 = -0.1278;

    const expectedBearing = 90.0; // Approximate bearing from Paris to London

    const calculatedBearing = calculateBearing(lat1, lon1, lat2, lon2);

    expect(calculatedBearing).toBeCloseTo(expectedBearing, 1); // Allowing for a small margin of error
  });

  it('should handle edge cases correctly', () => {
    const lat1 = 0; // Equator, Prime Meridian
    const lon1 = 0;
    const lat2 = 90; // North Pole
    const lon2 = 0;

    const expectedBearing = 0.0; // Bearing from equator to north pole should be 0 degrees

    const calculatedBearing = calculateBearing(lat1, lon1, lat2, lon2);

    expect(calculatedBearing).toBe(expectedBearing);
  });
});