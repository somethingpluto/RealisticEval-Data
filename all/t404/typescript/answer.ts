type Matrix = number[][];

function multiplyMatrices(A: Matrix, B: Matrix): Matrix {
    const result: Matrix = [];
    for (let i = 0; i < A.length; i++) {
        const row: number[] = [];
        for (let j = 0; j < B[0].length; j++) {
            let sum = 0;
            for (let k = 0; k < A[0].length; k++) {
                sum += A[i][k] * B[k][j];
            }
            row.push(sum);
        }
        result.push(row);
    }
    return result;
}

function power(matrix: Matrix, n: number): Matrix {
    if (n < 0) {
        throw new Error("The exponent n must be a non-negative integer.");
    }
    if (!Number.isInteger(n)) {
        throw new TypeError("The exponent n must be an integer.");
    }

    // Identity matrix of the same size as the input matrix
    const result: Matrix = matrix.map((_, i) => 
        matrix.map((_, j) => i === j ? 1 : 0)
    );

    let base = [...matrix];

    while (n > 0) {
        if (n % 2 === 1) {
            result = multiplyMatrices(result, base);
        }
        base = multiplyMatrices(base, base);
        n = Math.floor(n / 2);
    }

    return result;
}