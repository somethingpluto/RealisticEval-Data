function factorial(n: number): number {
    let result = 1;
    for (let i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}

function comb(n: number, k: number): number {
    return factorial(n) / (factorial(k) * factorial(n - k));
}

function pascalTriangleRow(i: number): number[] {
    /**
     * Generates the ith row of Pascal's Triangle.
     *
     * @param {number} i - Row index (0-indexed)
     * @return {number[]} An array representing the ith row of Pascal's Triangle
     */
    const row: number[] = [];
    for (let k = 0; k <= i; k++) {
        row.push(comb(i, k));
    }
    return row;
}
