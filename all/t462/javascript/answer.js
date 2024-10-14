function spiralOrder(matrix) {
    let result = [];
    while (matrix.length > 0) {
        // top row
        if (matrix[0].length > 0) {
            result.push(...matrix.shift());
        }

        // right column
        for (let i = 0; i < matrix.length - 1; i++) {
            if (matrix[i] && matrix[i].length > 0) {
                result.push(matrix[i].pop());
            }
        }

        // bottom row
        if (matrix[matrix.length - 1].length > 0) {
            result.push(...matrix.pop().reverse());
        }

        // left column
        for (let i = matrix.length - 1; i >= 0; i--) {
            if (matrix[i] && matrix[i].length > 0) {
                result.push(matrix[i].shift());
            }
        }
    }
    return result;
}