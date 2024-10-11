function power(matrix, n) {
    // Checks if input values are valid
    if (!Array.isArray(matrix) || !matrix.every(Array.isArray)) throw new Error('Matrix must be a 2D array');
    if (typeof n !== 'number' || n < 0) throw new Error('Exponent must be a non-negative number');

    // Initialize result as identity matrix
    let result = Array.from({length: matrix.length}, () => Array(matrix[0].length).fill(0));
    for(let i=0; i<matrix.length; i++) {
        result[i][i] = 1;
    }

    // Copy matrix to temp variable
    let temp = [...matrix];

    // Perform fast exponentiation
    while(n > 0) {
        if(n % 2 === 1) {
            result = multiplyMatrices(result, temp);
        }
        temp = multiplyMatrices(temp, temp);
        n = Math.floor(n / 2);
    }

    return result;
}