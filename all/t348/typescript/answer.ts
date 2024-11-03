/**
 * Find all prime numbers within a specified range.
 *
 * @param {number} lowerBound - The lower limit of the range (inclusive).
 * @param {number} upperBound - The upper limit of the range (inclusive).
 * @returns {number[]} A list containing all prime numbers within the specified range.
 */
function findPrimes(lowerBound: number, upperBound: number): number[] {
    const primes: number[] = [];

    for (let num = lowerBound; num <= upperBound; num++) {
        if (isPrime(num)) {
            primes.push(num);
        }
    }

    return primes;
}

/**
 * Helper function to determine if a number is prime.
 *
 * @param {number} num - The number to check for primality.
 * @returns {boolean} True if the number is prime, false otherwise.
 */
function isPrime(num: number): boolean {
    if (num < 2) return false; // 0 and 1 are not prime numbers
    for (let i = 2; i <= Math.sqrt(num); i++) {
        if (num % i === 0) return false; // If divisible, not prime
    }
    return true; // Number is prime
}