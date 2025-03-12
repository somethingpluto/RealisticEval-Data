// Start of the existing function for context
function cubicBezier(
    t: number,
    p0: [number, number],
    p1: [number, number],
    p2: [number, number],
    p3: [number, number]
): [number, number] {
    // ... (existing cubicBezier function code)

    // End of the existing function for context
}

// New function to calculate the length of the cubic Bézier curve
function bezierCurveLength(p0: [number, number], p1: [number, number], p2: [number, number], p3: [number, number]): number {
    const steps = 1000; // Number of steps to approximate the curve length
    let length = 0;
    let lastPoint = p0;

    for (let i = 0; i <= steps; i++) {
        const t = i / steps;
        const point = cubicBezier(t, p0, p1, p2, p3);
        length += Math.sqrt(Math.pow(point[0] - lastPoint[0], 2) + Math.pow(point[1] - lastPoint[1], 2));
        lastPoint = point;
    }

    return length;
}
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
