import {Matrix} from 'mathjs'
function getTranslation(matrix) {
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
