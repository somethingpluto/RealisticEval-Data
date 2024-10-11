function matrixMultiply(matrixA: number[][], matrixB: number[][]): number[][] {
    // Check if matrices can be multiplied
    if (matrixA[0].length !== matrixB.length) {
        throw new Error('Number of columns in matrixA must equal number of rows in matrixB');
    }

    let result: number[][] = Array.from({ length: matrixA.length }, () => Array(matrixB[0].length).fill(0));

    for(let i=0; i<matrixA.length; i++) {
        for(let j=0; j<matrixB[0].length; j++) {
            for(let k=0; k<matrixB.length; k++) {
                result[i][j] += matrixA[i][k] * matrixB[k][j];
            }
        }
    }

    return result;
}