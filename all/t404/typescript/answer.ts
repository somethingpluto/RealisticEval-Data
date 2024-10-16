function power(matrix: Matrix, n: number): Matrix {
    /**
     * Computes the n-th power of a matrix using the fast exponentiation method.
     *
     * @param {Matrix} matrix - A square matrix to be exponentiated.
     * @param {number} n - The exponent to raise the matrix to. Must be a non-negative integer.
     * @returns {Matrix} - The matrix raised to the power of n.
     * @throws {Error} - If n is negative.
     */
    
    if (n < 0) {
        throw new Error("The exponent must be a non-negative integer.");
    }

    const identity: Matrix = Array.from({ length: matrix.length }, () => 
        Array(matrix.length).fill(0).map((_, i) => (i === 0 ? 1 : 0))
    );

    let result: Matrix = identity;

    while (n > 0) {
        if (n % 2 === 1) {
            result = multiplyMatrices(result, matrix);
        }
        matrix = multiplyMatrices(matrix, matrix);
        n = Math.floor(n / 2);
    }

    return result;
}

function multiplyMatrices(a: Matrix, b: Matrix): Matrix {
    const result: Matrix = [];

    for (let i = 0; i < a.length; i++) {
        result.push([]);
        for (let j = 0; j < b[0].length; j++) {
            let sum = 0;
            for (let k = 0; k < b.length; k++) {
                sum += a[i][k] * b[k][j];
            }
            result[i].push(sum);
        }
    }

    return result;
}