describe('SeededRandom', () => {
    test('generates consistent numbers with the same seed', () => {
        const seededRand1 = new SeededRandom(42);
        const seededRand2 = new SeededRandom(42);

        expect(seededRand1.rand()).toBeCloseTo(seededRand2.rand(), 10);
        expect(seededRand1.rand()).toBeCloseTo(seededRand2.rand(), 10);
        expect(seededRand1.rand()).toBeCloseTo(seededRand2.rand(), 10);
    });

    test('generates different numbers with different seeds', () => {
        const seededRand1 = new SeededRandom(42);
        const seededRand2 = new SeededRandom(24);

        expect(seededRand1.rand()).not.toBeCloseTo(seededRand2.rand(), 10);
    });

    test('returns numbers between 0 and 1', () => {
        const seededRand = new SeededRandom(123456);

        for (let i = 0; i < 1000; i++) {
            const randValue = seededRand.rand();
            expect(randValue).toBeGreaterThanOrEqual(0);
            expect(randValue).toBeLessThan(1);
        }
    });

    test('produces different sequences with different seeds', () => {
        const seededRand1 = new SeededRandom(123);
        const seededRand2 = new SeededRandom(456);

        const sequence1 = Array.from({ length: 5 }, () => seededRand1.rand());
        const sequence2 = Array.from({ length: 5 }, () => seededRand2.rand());

        expect(sequence1).not.toEqual(sequence2);
    });

    test('consistent sequence with the same seed over multiple calls', () => {
        const seededRand = new SeededRandom(987654321);

        const sequence1 = [seededRand.rand(), seededRand.rand(), seededRand.rand()];

        // Re-initialize with the same seed to test consistency
        const seededRand2 = new SeededRandom(987654321);
        const sequence2 = [seededRand2.rand(), seededRand2.rand(), seededRand2.rand()];

        expect(sequence1).toEqual(sequence2);
    });
});