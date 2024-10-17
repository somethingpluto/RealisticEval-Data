function factorial(n) {
    let result = 1;
    for (let i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}

function comb(n, k) {
    return factorial(n) / (factorial(k) * factorial(n - k));
}

function pascalTriangleRow(i) {
    /**
     * Generates the ith row of Pascal's Triangle.
     *
     * @param {number} i - Row index (0-indexed)
     * @return {Array} An array representing the ith row of Pascal's Triangle
     */
    const row = [];
    for (let k = 0; k <= i; k++) {
        row.push(comb(i, k));
    }
    return row;
}