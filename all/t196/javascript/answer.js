/**
 * @brief Find all prime numbers that are less than or equal to limit using the Eichler sieve algorithm
 *
 * @param {number} limit The upper bound (inclusive) for finding prime numbers.
 * @return {number[]} An array of integers containing all prime numbers less than or equal to the limit.
 * @throws {Error} if the limit is less than 2.
 */
function generatePrimes(limit) {
    if (limit < 2) {
        throw new Error("Limit must be greater than or equal to 2.");
    }

    const isPrime = new Array(limit + 1).fill(true);
    isPrime[0] = isPrime[1] = false;  // 0 and 1 are not prime numbers

    for (let i = 2; i * i <= limit; i++) {
        if (isPrime[i]) {
            for (let j = i * i; j <= limit; j += i) {
                isPrime[j] = false;
            }
        }
    }

    const primes = [];
    for (let i = 2; i <= limit; i++) {
        if (isPrime[i]) {
            primes.push(i);
        }
    }

    return primes;
}