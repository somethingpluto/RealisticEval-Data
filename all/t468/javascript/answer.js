const { Matrix } = require('mathjs');

function getTranslation(matrix) {
    /**
     * Given a 3x3 matrix, return the corresponding translation vector.
     *
     * @param {Array<Array<number>>} matrix - A 3x3 affine transformation matrix.
     * @returns {Array<number>} A 2-element array containing the translation components (translation_x, translation_y).
     */

    if (!(matrix instanceof Matrix)) {
        throw new Error('Input must be a 3x3 matrix');
    }

    const m = matrix.toArray();
    if (m.length !== 9 || m[0].length !== 3) {
        throw new Error('Input must be a 3x3 matrix');
    }

    const translationX = m[2][0];
    const translationY = m[2][1];

    return [translationX, translationY];
}

// Example usage:
const matrix = new Matrix([
    [1, 0, 5],
    [0, 1, 10],
    [0, 0, 1]
]);

const translationVector = getTranslation(matrix);
console.log(translationVector); // Output: [5, 10]