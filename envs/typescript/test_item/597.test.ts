// Start of the TypeScript file

/**
 * Converts a hue value to its corresponding RGB color values.
 * ...
 */

// ... (rest of the TypeScript function)

// End of the TypeScript file
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
