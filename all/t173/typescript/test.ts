describe('Answer', () => {
    test('cubicBezier t=0', () => {
        const p0: [number, number] = [0.0, 0.0];
        const p1: [number, number] = [0.0, 1.0];
        const p2: [number, number] = [1.0, 1.0];
        const p3: [number, number] = [1.0, 0.0];

        const t = 0.0;
        const expected: [number, number] = [0.0, 0.0];
        expect(cubicBezier(t, p0, p1, p2, p3)).toEqual(expected);
    });

    test('cubicBezier t=1', () => {
        const p0: [number, number] = [0.0, 0.0];
        const p1: [number, number] = [0.0, 1.0];
        const p2: [number, number] = [1.0, 1.0];
        const p3: [number, number] = [1.0, 0.0];

        const t = 1.0;
        const expected: [number, number] = [1.0, 0.0];
        expect(cubicBezier(t, p0, p1, p2, p3)).toEqual(expected);
    });

    test('cubicBezier t=0.5', () => {
        const p0: [number, number] = [0.0, 0.0];
        const p1: [number, number] = [0.0, 1.0];
        const p2: [number, number] = [1.0, 1.0];
        const p3: [number, number] = [1.0, 0.0];

        const t = 0.5;
        const expected: [number, number] = [0.5, 0.75];
        expect(cubicBezier(t, p0, p1, p2, p3)).toBeCloseTo(expected[0], 9);
        expect(cubicBezier(t, p0, p1, p2, p3)[1]).toBeCloseTo(expected[1], 9);
    });

    test('cubicBezier midPoint', () => {
        const p0: [number, number] = [0.0, 0.0];
        const p1: [number, number] = [1.0, 1.0];
        const p2: [number, number] = [2.0, 1.0];
        const p3: [number, number] = [3.0, 0.0];

        const t = 0.5;
        const expected: [number, number] = [1.5, 0.75];
        expect(cubicBezier(t, p0, p1, p2, p3)).toBeCloseTo(expected[0], 9);
        expect(cubicBezier(t, p0, p1, p2, p3)[1]).toBeCloseTo(expected[1], 9);
    });

    test('cubicBezier arbitraryT', () => {
        const p0: [number, number] = [0.0, 0.0];
        const p1: [number, number] = [0.0, 2.0];
        const p2: [number, number] = [2.0, 2.0];
        const p3: [number, number] = [2.0, 0.0];

        const t = 0.75;
        const expected: [number, number] = [1.6875, 1.125];
        expect(cubicBezier(t, p0, p1, p2, p3)).toBeCloseTo(expected[0], 9);
        expect(cubicBezier(t, p0, p1, p2, p3)[1]).toBeCloseTo(expected[1], 9);
    });
});