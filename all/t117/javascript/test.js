describe('rgbToHsl function', () => {
    test('converts pure red to HSL', () => {
        expect(rgbToHsl(255, 0, 0)).toEqual({h: 0, s: 100, l: 50});
    });

    test('converts black to HSL', () => {
        expect(rgbToHsl(0, 0, 0)).toEqual({h: 0, s: 0, l: 0});
    });

    test('converts white to HSL', () => {
        expect(rgbToHsl(255, 255, 255)).toEqual({h: 0, s: 0, l: 100});
    });

    test('converts a color on the edge of RGB range', () => {
        expect(rgbToHsl(0, 255, 255)).toEqual({h: 180, s: 100, l: 50});
    });
});