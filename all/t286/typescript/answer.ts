function findLargestDivisible(n: number): number | null {
    // Start checking from n and go down to half of n
    const start = n;
    const end = Math.floor(n / 2);

    for (let i = start; i > end; i--) {
        if (i % 5 === 0) {
            return i;
        }
    }

    return null;  // Return null if no number divisible by 5 is found
}