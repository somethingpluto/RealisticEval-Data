const calculateRedProportion = require('./yourModule'); // Replace with the correct path to your function file

describe('calculateRedProportion', () => {
    test('all red pixels', () => {
        // All pixels are fully red
        const pixels = [[255, 0, 0], [255, 0, 0], [255, 0, 0]];
        const result = calculateRedProportion(pixels);
        expect(result).toBeCloseTo(1.0);
    });

    test('no red pixels', () => {
        // No red component in any pixel
        const pixels = [[0, 255, 0], [0, 0, 255], [0, 255, 255]];
        const result = calculateRedProportion(pixels);
        expect(result).toBeCloseTo(0.0);
    });

    test('empty pixel list', () => {
        // Empty list of pixels
        const pixels = [];
        const result = calculateRedProportion(pixels);
        expect(result).toBeCloseTo(0.0);
    });

    test('all black pixels', () => {
        // All pixels are black
        const pixels = [[0, 0, 0], [0, 0, 0], [0, 0, 0]];
        const result = calculateRedProportion(pixels);
        expect(result).toBeCloseTo(0.0);
    });
});