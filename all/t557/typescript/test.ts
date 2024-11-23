describe('radiansToDegrees', () => {
    it('should convert 0 radians to 0 degrees', () => {
        expect(radiansToDegrees(0)).toBeCloseTo(0, 5);
    });

    it('should convert π/2 radians to 90 degrees', () => {
        expect(radiansToDegrees(pi / 2)).toBeCloseTo(90, 5);
    });

    it('should convert π radians to 180 degrees', () => {
        expect(radiansToDegrees(pi)).toBeCloseTo(180, 5);
    });

    it('should convert 3π/2 radians to 270 degrees', () => {
        expect(radiansToDegrees(3 * pi / 2)).toBeCloseTo(270, 5);
    });

    it('should convert 2π radians to 360 degrees', () => {
        expect(radiansToDegrees(2 * pi)).toBeCloseTo(360, 5);
    });

    it('should convert -π/2 radians to -90 degrees', () => {
        expect(radiansToDegrees(-pi / 2)).toBeCloseTo(-90, 5);
    });

    it('should convert 4π radians to 720 degrees', () => {
        expect(radiansToDegrees(4 * pi)).toBeCloseTo(720, 5);
    });
});