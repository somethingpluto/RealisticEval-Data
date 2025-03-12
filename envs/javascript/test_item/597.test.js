/**
 * Converts a hue value to its corresponding RGB color values.
 *
 * @param {number} hue - A float representing the hue angle in degrees,
 *                       expected to be be in the range [0, 360).
 *
 * @return {Array<number>} An array containing three integers representing the
 *                         RGB color components in the range [0, 255]. The
 *                         first element is the red component, the second
 *                         element is the green component, and the third element
 *                         is the blue component.
 */
function hueToRGB(hue) {
    // Ensure the hue value is within the valid range [0, 360)
    hue = hue % 360;
    if (hue < 0) hue += 360;

    // Normalize the hue to the range [0, 1)
    let h = hue / 60.0;

    // Calculate the RGB components
    let r, g, b;
    let c = 1.0; // Chroma (maximum value for RGB components in this model)
    let x = c * (1 - Math.abs(h % 2 - 1));

    if (h >= 0 && h < 1) {
        r = c; g = x; b = 0;
    } else if (h >= 1 && h < 2) {
        r = x; g = c; b = 0;
    } else if (h >= 2 && h < 3) {
        r = 0; g = c; b = x;
    } else if (h >= 3 && h < 4) {
        r = 0; g = x; b = c;
    } else if (h >= 4 && h < 5) {
        r = x; g = 0; b = c;
    } else { // h >= 5 && h < 6
        r = c; g = 0; b = x;
    }

    // Adjust the RGB values to the range [0, 255]
    r = Math.round(r * 255);
    g = Math.round(g * 255);
    b = Math.round(b * 255);

    return [r, g, b];
}
describe("Hue to RGB Conversion Tests", () => {
    test("Hue 0 (Red)", () => {
        const [r, g, b] = hueToRGB(0);
        expect(r).toBe(255);
        expect(g).toBe(0);
        expect(b).toBe(0);
    });

    test("Hue 120 (Green)", () => {
        const [r, g, b] = hueToRGB(120);
        expect(r).toBe(0);
        expect(g).toBe(255);
        expect(b).toBe(0);
    });

    test("Hue 240 (Blue)", () => {
        const [r, g, b] = hueToRGB(240);
        expect(r).toBe(0);
        expect(g).toBe(0);
        expect(b).toBe(255);
    });

    test("Hue 60 (Yellow)", () => {
        const [r, g, b] = hueToRGB(60);
        expect(r).toBe(255);
        expect(g).toBe(255);
        expect(b).toBe(0);
    });

    test("Hue 180 (Cyan)", () => {
        const [r, g, b] = hueToRGB(180);
        expect(r).toBe(0);
        expect(g).toBe(255);
        expect(b).toBe(255);
    });

    test("Hue 300 (Magenta)", () => {
        const [r, g, b] = hueToRGB(300);
        expect(r).toBe(255);
        expect(g).toBe(0);
        expect(b).toBe(255);
    });
});
