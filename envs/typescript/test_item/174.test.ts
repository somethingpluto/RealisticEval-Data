// ... (previous code for context)

function findTForX(targetX: number, p0: number, p1: number, p2: number, tolerance: number = 1e-6, maxIterations: number = 100): number {
    let t0 = 0;
    let t1 = 1;
    let t = 0.5;
    let x = bezierX(t, p0, p1, p2);
    let iterations = 0;

    while (Math.abs(x - targetX) > tolerance && iterations < maxIterations) {
        if (x < targetX) {
            t0 = t;
            t = (t + t1) / 2;
        } else {
            t1 = t;
            t = (t0 + t) / 2;
        }
        x = bezierX(t, p0, p1, p2);
        iterations++;
    }

    return t;
}

// ... (rest of the code)
describe('TestfindTForX', () => {
    // Tolerance level for floating-point comparisons
    const TOLERANCE = 1e-6;

    test('findTForX should return 0.0 when targetX is at the start', () => {
        const p0 = 0.0;
        const p1 = 0.5;
        const p2 = 1.0;
        const targetX = 0.0;

        const t = findTForX(targetX, p0, p1, p2);
        expect(t).toBeCloseTo(0.0, TOLERANCE);
    });

    test('findTForX should return 1.0 when targetX is at the end', () => {
        const p0 = 0.0;
        const p1 = 0.5;
        const p2 = 1.0;
        const targetX = 1.0;

        const t = findTForX(targetX, p0, p1, p2);
        expect(t).toBeCloseTo(1.0, TOLERANCE);
    });

    test('findTForX should return 0.25 when targetX is mid-curve', () => {
        const p0 = 0.0;
        const p1 = 0.5;
        const p2 = 1.0;
        const targetX = 0.25;

        const t = findTForX(targetX, p0, p1, p2);
        expect(t).toBeCloseTo(0.25, TOLERANCE);
    });

    test('findTForX should return 0.75 when targetX is near mid-curve', () => {
        const p0 = 0.0;
        const p1 = 1.0;
        const p2 = 2.0;
        const targetX = 1.5;

        const t = findTForX(targetX, p0, p1, p2);
        expect(t).toBeCloseTo(0.75, TOLERANCE);
    });
});
