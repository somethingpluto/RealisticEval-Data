describe('TestCalculateBearing', () => {
    it('should calculate north bearing correctly', () => {
        // From equator directly north
        expect(calculateBearing(0, 0, 10, 0)).toBeCloseTo(0);
    });

    it('should calculate east bearing correctly', () => {
        // From prime meridian directly east
        expect(calculateBearing(0, 0, 0, 10)).toBeCloseTo(90);
    });

    it('should calculate south bearing correctly', () => {
        // From a point directly south
        expect(calculateBearing(10, 0, 0, 0)).toBeCloseTo(180);
    });

    it('should calculate west bearing correctly', () => {
        // From a point directly west
        expect(calculateBearing(0, 10, 0, 0)).toBeCloseTo(270);
    });

    it('should calculate bearing across prime meridian correctly', () => {
        // From a point west of the prime meridian to a point east
        expect(calculateBearing(0, -1, 0, 1)).toBeCloseTo(90);
    });
});