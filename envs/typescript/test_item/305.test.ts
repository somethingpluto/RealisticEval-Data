import { v4 as uuidv4 } from 'uuid';

class SeededRandom {
    // ... (rest of the class)

    /**
     * Generates a random integer between min (inclusive) and max (inclusive).
     * @param min - The minimum value (inclusive).
     * @param max - The maximum value (inclusive).
     * @returns A pseudo-random integer between min and max.
     */
    randInt(min: number, max: number): number {
        return Math.floor(this.rand() * (max - min + 1)) + min;
    }

    /**
     * Generates a random hexadecimal string of the specified length.
     * @param length - The length of the hexadecimal string to generate.
     * @returns A pseudo-random hexadecimal string.
     */
    randHex(length: number): string {
        let result = '';
        const characters = '0123456789abcdef';
        for (let i = 0; i < length; i++) {
            result += characters.charAt(Math.floor(this.rand() * characters.length));
        }
        return result;
    }
}
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
