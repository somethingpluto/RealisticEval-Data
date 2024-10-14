const math = require('mathjs');

/**
 * Compares two sets of floats for equality within a relative and absolute tolerance.
 *
 * @param {Set<number>} set1 - The first set of floats.
 * @param {Set<number>} set2 - The second set of floats.
 * @param {number} [rtol=1e-5] - The relative tolerance (default: 1e-5).
 * @param {number} [atol=1e-6] - The absolute tolerance (default: 1e-6).
 * @returns {boolean} True if the sets are equal within the specified tolerances, False otherwise.
 */
function areSetsEqual(set1, set2, rtol = 1e-5, atol = 1e-6) {
    // Convert sets to sorted arrays for comparison
    const list1 = Array.from(set1).sort((a, b) => a - b);
    const list2 = Array.from(set2).sort((a, b) => a - b);

    // Check if the lengths of both sets are the same
    if (list1.length !== list2.length) {
        return false;
    }

    // Compare each element in the two sorted arrays
    for (let i = 0; i < list1.length; i++) {
        if (!math.isEqual(math.bignumber(list1[i]), math.bignumber(list2[i]), { rtol, atol })) {
            return false;
        }
    }

    return true;
}