// ... (previous code for context)
function rgbToHsl(r: number, g: number, b: number): { h: number; s: number; l: number } {
  // ... (existing function body)

  // Convert HSL to HEX
  function hslToHex(h: number, s: number, l: number): string {
    const c = (1 - Math.abs(2 * l - 1)) * s;
    const x = c * (1 - Math.abs((h / 60) % 2 - 1));
    const m = l - c / 2;
    let r = 0, g = 0, b = 0;

    if (0 <= h && h < 60) {
      [r, g, b] = [c, x, 0];
    } else if (60 <= h && h < 120) {
      [r, g, b] = [x, c, 0];
    } else if (120 <= h && h < 180) {
      [r, g, b] = [0, c, x];
    } else if (180 <= h && h < 240) {
      [r, g, b] = [0, x, c];
    } else if (240 <= h && h < 300) {
      [r, g, b] = [x, 0, c];
    } else {
      [r, g, b] = [c, 0, x];
    }

    return `#${Math.round((r + m) * 255).toString(16).padStart(2, '0')}${Math.round((g + m) * 255).toString(16).padStart(2, '0')}${Math.round((b + m) * 255).toString(16).padStart(2, '0')}`;
  }

  return { h, s, l, hex: hslToHex(h, s, l) };
}
// ... (rest of the code)
describe('rgbToHsl function', () => {
    test('converts pure red to HSL', () => {
        expect(rgbToHsl(255, 0, 0)).toEqual({ h: 0, s: 100, l: 50 });
    });

    test('converts black to HSL', () => {
        expect(rgbToHsl(0, 0, 0)).toEqual({ h: 0, s: 0, l: 0 });
    });

    test('converts white to HSL', () => {
        expect(rgbToHsl(255, 255, 255)).toEqual({ h: 0, s: 0, l: 100 });
    });

    test('converts a color on the edge of RGB range', () => {
        expect(rgbToHsl(0, 255, 255)).toEqual({ h: 180, s: 100, l: 50 });
    });
});
