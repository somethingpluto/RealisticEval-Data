/**
 * Generates all unique combinations of pairs from an array.
 *
 * @param {Array} array - The input array from which combinations are generated.
 * @returns {Array} - An array of arrays, where each inner array contains a unique pair of elements.
 */
function generateUniquePairs(array) {
    const pairs = [];
    const length = array.length;

    for (let i = 0; i < length; i++) {
        for (let j = i + 1; j < length; j++) {
            pairs.push([array[i], array[j]]);
        }
    }

    return pairs;
}