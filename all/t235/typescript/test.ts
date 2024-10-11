const approximatelyEqual = (a, b, epsilon = 1e-9) => Math.abs(a - b) < epsilon;

describe('Calculate Bearing Tests', () => {
    test('North Bearing', () => {
        // From equator directly north
        expect(calculateBearing(0, 0, 10, 0)).toBeCloseTo(0, 9);
    });

    test('East Bearing', () => {
        // From prime meridian directly east
        expect(calculateBearing(0, 0, 0, 10)).toBeCloseTo(90, 9);
    });

    test('South Bearing', () => {
        // From a point directly south
        expect(calculateBearing(10, 0, 0, 0)).toBeCloseTo(180, 9);
    });

    test('West Bearing', () => {
        // From a point directly west
        expect(calculateBearing(0, 10, 0, 0)).toBeCloseTo(270, 9);
    });

    test('Across Prime Meridian', () => {
        // From a point west of the prime meridian to a point east
        expect(calculateBearing(0, -1, 0, 1)).toBeCloseTo(90, 9);
    });
});