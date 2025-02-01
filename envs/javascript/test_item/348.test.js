/**
 * Find all prime numbers within a specified range.
 *
 * @param {number} lowerBound - The lower limit of the range (inclusive).
 * @param {number} upperBound - The upper limit of the range (inclusive).
 * @returns {Array<number>} A list containing all prime numbers within the specified range.
 */
function findPrimes(lowerBound, upperBound) {
    const primes = [];
    for (let num = lowerBound; num <= upperBound; num++) {
        if (isPrime(num)) {
            primes.push(num);
        }
    }
    return primes;
}

function isPrime(num) {
    if (num <= 1) return false;
    if (num <= 3) return true;
    if (num % 2 === 0 || num % 3 === 0) return false;
    for (let i = 5; i * i <= num; i += 6) {
        if (num % i === 0 || num % (i + 2) === 0) return false;
    }
    return true;
}
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
