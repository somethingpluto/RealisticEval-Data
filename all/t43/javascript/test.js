const rgbToHsv = require('./yourModule'); // Adjust the path to your module containing the rgbToHsv function

describe('rgbToHsv', () => {

    test('converts pure red color', () => {
        const r = 255, g = 0, b = 0;
        const expected_result = [0, 1, 1]; // Hue should be 0, Saturation 1, Value 1 for red
        const result = rgbToHsv(r, g, b);
        expect(result).toEqual(expected_result);
    });

    test('converts pure green color', () => {
        const r = 0, g = 255, b = 0;
        const expected_result = [120, 1, 1]; // Hue should be 120, Saturation 1, Value 1 for green
        const result = rgbToHsv(r, g, b);
        expect(result).toEqual(expected_result);
    });

    test('converts pure blue color', () => {
        const r = 0, g = 0, b = 255;
        const expected_result = [240, 1, 1]; // Hue should be 240, Saturation 1, Value 1 for blue
        const result = rgbToHsv(r, g, b);
        expect(result).toEqual(expected_result);
    });

    test('converts white color', () => {
        const r = 255, g = 255, b = 255;
        const expected_result = [0, 0, 1]; // Hue is undefined, typically 0; Saturation 0, Value 1 for white
        const result = rgbToHsv(r, g, b);
        expect(result).toEqual(expected_result);
    });

    test('converts black color', () => {
        const r = 0, g = 0, b = 0;
        const expected_result = [0, 0, 0]; // Hue is undefined, typically 0; Saturation 0, Value 0 for black
        const result = rgbToHsv(r, g, b);
        expect(result).toEqual(expected_result);
    });

});