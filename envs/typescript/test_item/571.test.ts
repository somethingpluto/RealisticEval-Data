// Start of the code context
import { isNumber, isFinite } from 'util';

function isValidCoordinate(coord: string): boolean {
    const parts = coord.split(',');
    if (parts.length !== 2) return false;

    const lat = parseFloat(parts[0]);
    const lon = parseFloat(parts[1]);

    return isNumber(lat) && isFinite(lat) && lat >= -90 && lat <= 90 &&
           isNumber(lon) && isFinite(lon) && lon >= -180 && lon <= 180;
}
// End of the code context
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
