import { calculateRedProportion } from './yourModule';  // Make sure to import the function from its module

describe('calculateRedProportion', () => {
  
    test('all red pixels', () => {
        // All pixels are fully red
        const pixels: [number, number, number][] = [[255, 0, 0], [255, 0, 0], [255, 0, 0]];
        const result = calculateRedProportion(pixels);
        expect(result).toBeCloseTo(1.0);
    });

    test('no red pixels', () => {
        // No red component in any pixel
        const pixels: [number, number, number][] = [[0, 255, 0], [0, 0, 255], [0, 255, 255]];
        const result = calculateRedProportion(pixels);
        expect(result).toBeCloseTo(0.0);
    });

    test('empty pixel list', () => {
        // Empty list of pixels
        const pixels: [number, number, number][] = [];
        const result = calculateRedProportion(pixels);
        expect(result).toBeCloseTo(0.0);
    });

    test('all black pixels', () => {
        // All pixels are black
        const pixels: [number, number, number][] = [[0, 0, 0], [0, 0, 0], [0, 0, 0]];
        const result = calculateRedProportion(pixels);
        expect(result).toBeCloseTo(0.0);
    });

});