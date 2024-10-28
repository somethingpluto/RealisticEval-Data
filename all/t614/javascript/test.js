describe('calculateAverageDifference', () => {
    test('calculates average difference for positive integers', () => {
        const numbers = [10, 20, 30, 40];
        const result = calculateAverageDifference(numbers);
        const expected = 10.0;
        expect(result).toBeCloseTo(expected, 5); // Jest equivalent for almost equal assertion
    });

    test('calculates average difference for mixed positive and negative integers', () => {
        const numbers = [-10, 0, 10, 20];
        const result = calculateAverageDifference(numbers);
        const expected = 10.0;
        expect(result).toBeCloseTo(expected, 5); // Jest equivalent for almost equal assertion
    });

    test('calculates average difference for same values', () => {
        const numbers = [5, 5, 5, 5];
        const result = calculateAverageDifference(numbers);
        const expected = 0.0;
        expect(result).toBeCloseTo(expected, 5); // Jest equivalent for almost equal assertion
    });

    test('returns 0 for single element list', () => {
        const numbers = [100];
        const result = calculateAverageDifference(numbers);
        const expected = 0.0; // Not enough data to calculate differences
        expect(result).toBeCloseTo(expected, 5); // Jest equivalent for almost equal assertion
    });

    test('returns 0 for empty list', () => {
        const numbers = [];
        const result = calculateAverageDifference(numbers);
        const expected = 0.0; // Not enough data to calculate differences
        expect(result).toBeCloseTo(expected, 5); // Jest equivalent for almost equal assertion
    });
});