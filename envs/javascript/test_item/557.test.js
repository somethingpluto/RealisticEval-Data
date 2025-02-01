/**
 * Convert an angle from radians to degrees.
 * 
 * @param {number} radians - The angle in radians to convert.
 * @return {number} The angle in degrees.
 */
function radiansToDegrees(radians) {
    return radians * (180 / Math.PI);
}
describe('TestRadiansToDegrees', () => {
    it('test conversion of 0 radians', () => {
        expect(radiansToDegrees(0)).toBeCloseTo(0, 5);
    });

    it('test conversion of π/2 radians', () => {
        expect(radiansToDegrees(Math.PI / 2)).toBeCloseTo(90, 5);
    });

    it('test conversion of π radians', () => {
        expect(radiansToDegrees(Math.PI)).toBeCloseTo(180, 5);
    });

    it('test conversion of 3π/2 radians', () => {
        expect(radiansToDegrees(3 * Math.PI / 2)).toBeCloseTo(270, 5);
    });

    it('test conversion of 2π radians', () => {
        expect(radiansToDegrees(2 * Math.PI)).toBeCloseTo(360, 5);
    });

    it('test conversion of -π/2 radians', () => {
        expect(radiansToDegrees(-Math.PI / 2)).toBeCloseTo(-90, 5);
    });

    it('test conversion of a large angle (4π radians)', () => {
        expect(radiansToDegrees(4 * Math.PI)).toBeCloseTo(720, 5);
    });
});
