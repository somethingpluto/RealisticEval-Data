describe('hslToRgb', () => {
    test('Converts black (0% lightness)', () => {
        expect(hslToRgb(0, 0, 0)).toEqual({ r: 0, g: 0, b: 0 });
    });

    test('Converts white (100% lightness)', () => {
        expect(hslToRgb(0, 0, 1)).toEqual({ r: 255, g: 255, b: 255 });
    });

    test('Converts red (hue at 0)', () => {
        expect(hslToRgb(0, 1, 0.5)).toEqual({ r: 255, g: 0, b: 0 });
    });

    test('Converts green (hue at 120)', () => {
        expect(hslToRgb(120, 1, 0.5)).toEqual({ r: 0, g: 255, b: 0 });
    });

    test('Converts blue (hue at 240)', () => {
        expect(hslToRgb(240, 1, 0.5)).toEqual({ r: 0, g: 0, b: 255 });
    });

    test('Handles edge case with maximum hue (360 equivalent to 0)', () => {
        expect(hslToRgb(360, 1, 0.5)).toEqual({ r: 255, g: 0, b: 0 });
    });
});