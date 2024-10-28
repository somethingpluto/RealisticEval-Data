describe('findPrimes', () => {
    test('find primes in range', () => {
        const expected = [2, 3, 5, 7, 11];
        expect(findPrimes(1, 12)).toEqual(expected);
    });

    test('find single prime', () => {
        const expected = [29];
        expect(findPrimes(29, 29)).toEqual(expected);
    });

    test('find primes in big range', () => {
        const expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97];
        expect(findPrimes(1, 100)).toEqual(expected);
    });

    test('find no primes', () => {
        const expected = [];
        expect(findPrimes(0, 1)).toEqual(expected);
    });
});