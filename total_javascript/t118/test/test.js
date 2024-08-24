// Import the function if it's in another file
// const hslToRgb = require('./path_to_your_function');

describe('hslToRgb', () => {
    test('converts HSL black (0, 0%, 0%) to RGB (0, 0, 0)', () => {
        const { r, g, b } = hslToRgb(0, 0, 0);
        expect(r).toBe(0);
        expect(g).toBe(0);
        expect(b).toBe(0);
    });

    test('converts HSL white (0, 0%, 100%) to RGB (255, 255, 255)', () => {
        const { r, g, b } = hslToRgb(0, 0, 100);
        expect(r).toBe(255);
        expect(g).toBe(255);
        expect(b).toBe(255);
    });

    test('converts HSL red (0, 100%, 50%) to RGB (255, 0, 0)', () => {
        const { r, g, b } = hslToRgb(0, 100, 50);
        expect(r).toBe(255);
        expect(g).toBe(0);
        expect(b).toBe(0);
    });

    test('converts HSL green (120, 100%, 50%) to RGB (0, 255, 0)', () => {
        const { r, g, b } = hslToRgb(120, 100, 50);
        expect(r).toBe(0);
        expect(g).toBe(255);
        expect(b).toBe(0);
    });

    test('converts HSL blue (240, 100%, 50%) to RGB (0, 0, 255)', () => {
        const { r, g, b } = hslToRgb(240, 100, 50);
        expect(r).toBe(0);
        expect(g).toBe(0);
        expect(b).toBe(255);
    });
});
