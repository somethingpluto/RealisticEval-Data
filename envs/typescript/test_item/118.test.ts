// ... (previous code for context)
function hslToRgb(h: number, s: number, l: number): { r: number, g: number, b: number } {
    // ... (existing function code)

    // Convert the hue to a value between 0 and 1
    let hue = h / 360;

    // ... (existing function code)

    // Convert the RGB values to the range 0-255
    let r = Math.round(rgbR * 255);
    let g = Math.round(rgbG * 255);
    let b = Math.round(rgbB * 255);

    // Return the RGB values as an object
    return { r, g, b };
}
// ... (rest of the code)
describe('hslToRgb function', () => {
    test('converts pure red hue correctly', () => {
        expect(hslToRgb(0, 100, 50)).toEqual({ r: 255, g: 0, b: 0 });
    });

    test('returns gray for zero saturation', () => {
        expect(hslToRgb(240, 0, 50)).toEqual({ r: 128, g: 128, b: 128 });
    });

    test('returns white for full lightness', () => {
        expect(hslToRgb(120, 50, 100)).toEqual({ r: 255, g: 255, b: 255 });
    });

    test('converts full saturation and mid lightness blue correctly', () => {
        expect(hslToRgb(240, 100, 50)).toEqual({ r: 0, g: 0, b: 255 });
    });

    test('handles edge hue at 360 degrees correctly', () => {
        expect(hslToRgb(360, 100, 50)).toEqual({ r: 255, g: 0, b: 0 }); // Should be the same as hue 0
    });
});
