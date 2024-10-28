describe('findPrimes', () => {
    test('should find primes in range 1 to 12', () => {
        const expected = [2, 3, 5, 7, 11];
        expect(findPrimes(1, 12)).toEqual(expected);
    });

    test('should find a single prime number', () => {
        const expected = [29];
        expect(findPrimes(29, 29)).toEqual(expected);
    });

    test('should find primes in a big range 1 to 100', () => {
        const expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97];
        expect(findPrimes(1, 100)).toEqual(expected);
    });

    test('should return an empty array for range with no primes', () => {
        const expected: number[] = [];
        expect(findPrimes(0, 1)).toEqual(expected);
    });
});