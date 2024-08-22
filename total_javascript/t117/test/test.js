describe('rgbToHsl', () => {
    test('converts RGB black (0, 0, 0) to HSL', () => {
        const { h, s, l } = rgbToHsl(0, 0, 0);
        expect(h).toBe(0);
        expect(s).toBe(0);
        expect(l).toBe(0);
    });

    test('converts RGB white (255, 255, 255) to HSL', () => {
        const { h, s, l } = rgbToHsl(255, 255, 255);
        expect(h).toBe(0);
        expect(s).toBe(0);
        expect(l).toBe(100);
    });

    test('converts RGB red (255, 0, 0) to HSL', () => {
        const { h, s, l } = rgbToHsl(255, 0, 0);
        expect(h).toBe(0);
        expect(s).toBe(100);
        expect(l).toBe(50); // Close to 0.5 lightness
    });

    test('converts RGB green (0, 255, 0) to HSL', () => {
        const { h, s, l } = rgbToHsl(0, 255, 0);
        expect(h).toBe(120); // Close to 120 hue for green
        expect(s).toBe(100);
        expect(l).toBe(50); // Close to 0.5 lightness
    });

    test('converts RGB blue (0, 0, 255) to HSL', () => {
        const { h, s, l } = rgbToHsl(0, 0, 255);
        expect(h).toBe(240); // Close to 240 hue for blue
        expect(s).toBe(100);
        expect(l).toBe(50); // Close to 0.5 lightness
    });
});