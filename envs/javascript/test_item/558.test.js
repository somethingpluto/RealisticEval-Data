/**
 * Convert an angle from degrees to radians.
 * 
 * @param {number} degrees - The angle in degrees to convert.
 * @returns {number} The angle in radians.
 */
function degreesToRadians(degrees) {
    return degrees * (Math.PI / 180);
}
describe('TestDegreesToRadians', () => {
    it('test conversion of 0 degrees', () => {
        expect(degreesToRadians(0)).toBeCloseTo(0, 5);
    });

    it('test conversion of 90 degrees', () => {
        expect(degreesToRadians(90)).toBeCloseTo(Math.PI / 2, 5);
    });

    it('test conversion of 180 degrees', () => {
        expect(degreesToRadians(180)).toBeCloseTo(Math.PI, 5);
    });

    it('test conversion of 270 degrees', () => {
        expect(degreesToRadians(270)).toBeCloseTo(3 * Math.PI / 2, 5);
    });

    it('test conversion of 360 degrees', () => {
        expect(degreesToRadians(360)).toBeCloseTo(2 * Math.PI, 5);
    });

    it('test conversion of negative degrees', () => {
        expect(degreesToRadians(-90)).toBeCloseTo(-Math.PI / 2, 5);
    });

    it('test conversion of a large angle (720 degrees)', () => {
        expect(degreesToRadians(720)).toBeCloseTo(4 * Math.PI, 5);
    });
});
