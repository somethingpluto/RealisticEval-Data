function multiplyMatrices(A, B) {
    // Multiplies two matrices A and B and returns the result.
    return A.map(A_row => 
        B[0].map((_, colIndex) => 
            A_row.reduce((sum, a, rowIndex) => 
                sum + a * B[rowIndex][colIndex], 0)
        )
    );
}

function power(matrix, n) {
    if (n < 0) {
        throw new Error("The exponent n must be a non-negative integer.");
    }
    if (!Number.isInteger(n)) {
        throw new TypeError("The exponent n must be an integer.");
    }

    // Identity matrix of the same size as the input matrix
    const size = matrix.length;
    const result = Array.from({ length: size }, (_, i) =>
        Array.from({ length: size }, (_, j) => (i === j ? 1 : 0))
    );

    let base = matrix.map(row => row.slice());

    while (n > 0) {
        if (n % 2 === 1) {
            result = multiplyMatrices(result, base);
        }
        base = multiplyMatrices(base, base);
        n = Math.floor(n / 2);
    }

    return result;
}