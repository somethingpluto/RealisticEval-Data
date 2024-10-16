describe('cubicBezier', () => {
    test('t = 0', () => {
        const p0 = [0.0, 0.0];
        const p1 = [0.0, 1.0];
        const p2 = [1.0, 1.0];
        const p3 = [1.0, 0.0];
        const t = 0.0;
        const expected = [0.0, 0.0];
        expect(cubicBezier(t, p0, p1, p2, p3)).toEqual(expected);
    });

    test('t = 1', () => {
        const p0 = [0.0, 0.0];
        const p1 = [0.0, 1.0];
        const p2 = [1.0, 1.0];
        const p3 = [1.0, 0.0];
        const t = 1.0;
        const expected = [1.0, 0.0];
        expect(cubicBezier(t, p0, p1, p2, p3)).toEqual(expected);
    });

    test('t = 0.5', () => {
        const p0 = [0.0, 0.0];
        const p1 = [0.0, 1.0];
        const p2 = [1.0, 1.0];
        const p3 = [1.0, 0.0];
        const t = 0.5;
        const expected = [0.5, 0.75];
        expect(cubicBezier(t, p0, p1, p2, p3)).toBeCloseTo(expected[0], 9);
        expect(cubicBezier(t, p0, p1, p2, p3)).toBeCloseTo(expected[1], 9);
    });

    test('t = 0.5 with mid points', () => {
        const p0 = [0.0, 0.0];
        const p1 = [1.0, 1.0];
        const p2 = [2.0, 1.0];
        const p3 = [3.0, 0.0];
        const t = 0.5;
        const expected = [1.5, 0.75];
        expect(cubicBezier(t, p0, p1, p2, p3)).toBeCloseTo(expected[0], 9);
        expect(cubicBezier(t, p0, p1, p2, p3)).toBeCloseTo(expected[1], 9);
    });

    test('arbitrary t = 0.75', () => {
        const p0 = [0.0, 0.0];
        const p1 = [0.0, 2.0];
        const p2 = [2.0, 2.0];
        const p3 = [2.0, 0.0];
        const t = 0.75;
        const expected = [1.6875, 1.125];
        expect(cubicBezier(t, p0, p1, p2, p3)).toBeCloseTo(expected[0], 9);
        expect(cubicBezier(t, p0, p1, p2, p3)).toBeCloseTo(expected[1], 9);
    });
});