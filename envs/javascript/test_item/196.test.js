/**
 * Find all prime numbers that are less than or equal to limit using the Eichler sieve algorithm
 *
 * @param {number} limit The upper bound (inclusive) for finding prime numbers.
 * @return {number[]} An array of integers containing all prime numbers less than or equal to the limit.
 * @throws {Error} if the limit is less than 2.
 */
function generatePrimes(limit) {
  if (limit < 2) {
    throw new Error('Limit must be greater than or equal to 2.');
  }

  const primes = [];
  const sieve = new Array(limit + 1).fill(true);
  sieve[0] = sieve[1] = false;

  for (let i = 2; i <= Math.sqrt(limit); i++) {
    if (sieve[i]) {
      primes.push(i);
      for (let j = i * i; j <= limit; j += i) {
        sieve[j] = false;
      }
    }
  }

  for (let i = Math.sqrt(limit) + 1; i <= limit; i++) {
    if (sieve[i]) {
      primes.push(i);
    }
  }

  return primes;
}
describe("Sieve of Eratosthenes Test Cases", () => {
    // Test Case 1: Small limit (10)
    test("should return primes less than or equal to 10", () => {
        const expected1 = [2, 3, 5, 7];
        expect(generatePrimes(10)).toEqual(expected1);
    });

    // Test Case 2: Prime limit (29)
    test("should return primes less than or equal to 29", () => {
        const expected2 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29];
        expect(generatePrimes(29)).toEqual(expected2);
    });

    // Test Case 3: Non-prime limit (30)
    test("should return primes less than or equal to 30", () => {
        const expected3 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29];
        expect(generatePrimes(30)).toEqual(expected3);
    });

    // Test Case 4: Limit of 2 (smallest prime)
    test("should return [2] for limit 2", () => {
        const expected4 = [2];
        expect(generatePrimes(2)).toEqual(expected4);
    });

    // Test Case 5: Invalid limit (1, should throw an exception)
    test("should throw an error for limit less than 2", () => {
        expect(() => generatePrimes(1)).toThrow("Limit must be greater than or equal to 2.");
    });
});
