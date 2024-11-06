function findPowers(num) {
    if (num <= 0) {
        throw new Error("Input must be a positive integer greater than zero.");
    }

    let n = 0;  // Initialize counter for powers of 2
    let m = 0;  // Initialize counter for powers of 3

    // Count the power of 2 in the factorization
    while (num % 2 === 0) {
        n += 1;
        num = Math.floor(num / 2);
    }

    // Count the power of 3 in the factorization
    while (num % 3 === 0) {
        m += 1;
        num = Math.floor(num / 3);
    }

    // If num is reduced to 1, only 2's and 3's were factors
    if (num === 1) {
        return [n, m];
    } else {
        return null;  // Return null if there are other prime factors
    }
}