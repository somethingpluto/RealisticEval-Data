/**
 * Checks if the string conforms to the latitude and longitude identification specification.
 *
 * @param {string} coord - The coordinate string to check (can be latitude or longitude).
 * @returns {boolean} A boolean indicating whether the coordinate is valid.
 */
function isValidCoordinate(coord) {
    // Regular expression to match valid latitude or longitude formats
    const regex = /^-?(([1-8]?[0-9](\.\d+)?)|(90(\.0+)?)),\s*-?((((1[0-7][0-9])|([1-9]?[0-9]))(\.\d+)?)|(180(\.0+)?))/;
    
    // Test the coordinate against the regex
    return regex.test(coord);
}
describe('isValidCoordinate', () => {
    test('valid latitude with direction', () => {
        const coord = "45.123N";
        expect(isValidCoordinate(coord)).toBe(true);
    });

    test('valid latitude without direction', () => {
        const coord = "90.0";
        expect(isValidCoordinate(coord)).toBe(true);
    });

    test('valid longitude with direction', () => {
        const coord = "180.0E";
        expect(isValidCoordinate(coord)).toBe(true);
    });

    test('valid longitude without direction', () => {
        const coord = "-120.456";
        expect(isValidCoordinate(coord)).toBe(true);
    });

    test('invalid longitude exceeding range', () => {
        const coord = "-200.5";
        expect(isValidCoordinate(coord)).toBe(false);
    });
});
