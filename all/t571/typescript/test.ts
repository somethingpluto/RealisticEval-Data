describe('isValidCoordinate', () => {
    test('valid latitude with direction', () => {
        const coord = "45.123N";
        expect(isValidCoordinate(coord)).toBe(true);
    });

    test('valid latitude without direction', () => {
        const coord = "90.0";
        expect(isValidCoordinate(coord)).toBe(true);
    });

    test('valid longitude with direction', () => {
        const coord = "180.0E";
        expect(isValidCoordinate(coord)).toBe(true);
    });

    test('valid longitude without direction', () => {
        const coord = "-120.456";
        expect(isValidCoordinate(coord)).toBe(true);
    });


    test('invalid longitude exceeding range', () => {
        const coord = "-200.5";
        expect(isValidCoordinate(coord)).toBe(false);
    });
});