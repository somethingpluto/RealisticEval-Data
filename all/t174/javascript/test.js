describe('TestFindTForX', () => {
    test('findTForX at start', () => {
        const p0 = 0.0, p1 = 0.5, p2 = 1.0;
        const targetX = 0.0;
        const t = findTForX(targetX, p0, p1, p2);
        expect(t).toBeCloseTo(0.0, TOLERANCE);
    });

    test('findTForX at end', () => {
        const p0 = 0.0, p1 = 0.5, p2 = 1.0;
        const targetX = 1.0;
        const t = findTForX(targetX, p0, p1, p2);
        expect(t).toBeCloseTo(1.0, TOLERANCE);
    });

    test('findTForX mid curve', () => {
        const p0 = 0.0, p1 = 0.5, p2 = 1.0;
        const targetX = 0.25;
        const t = findTForX(targetX, p0, p1, p2);
        expect(t).toBeCloseTo(0.25, TOLERANCE);
    });

    test('findTForX near mid curve', () => {
        const p0 = 0.0, p1 = 1.0, p2 = 2.0;
        const targetX = 1.5;
        const t = findTForX(targetX, p0, p1, p2);
        expect(t).toBeCloseTo(0.75, TOLERANCE);
    });
});