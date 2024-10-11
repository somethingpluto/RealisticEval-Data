function findLargestDivisible(n: number): number | null {
    /**
     * Find the largest integer between a given number n and half of it that is divisible by 10 or 5
     *
     * @param {number} n - The upper bound of the range.
     * @returns {number | null} - The largest integer between n and half of n that is divisible by 5, or null if no such number exists.
     */

    let lowerBound = Math.floor(n / 2);

    while (lowerBound < n) {
        if (lowerBound % 10 === 0 || lowerBound % 5 === 0) {
            return lowerBound;
        }
        lowerBound++;
    }

    return null;
}