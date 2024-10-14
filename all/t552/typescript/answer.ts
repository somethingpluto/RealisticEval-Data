import { isEqualWith, property } from 'lodash';

/**
 * Compares two sets of floats for equality within a relative and absolute tolerance.
 *
 * @param set1 - The first set of floats.
 * @param set2 - The second set of floats.
 * @param rtol - The relative tolerance (default: 1e-5).
 * @param atol - The absolute tolerance (default: 1e-6).
 * @returns True if the sets are equal within the specified tolerances, False otherwise.
 */
function areSetsEqual(set1: Set<number>, set2: Set<number>, rtol: number = 1e-5, atol: number = 1e-6): boolean {
    // Convert sets to sorted arrays for comparison
    const list1 = Array.from(set1).sort((a, b) => a - b);
    const list2 = Array.from(set2).sort((a, b) => a - b);

    // Check if the lengths of both sets are the same
    if (list1.length !== list2.length) {
        return false;
    }

    // Define a custom comparator function using lodash's isEqualWith
    const customComparator = isEqualWith((a: number, b: number) => {
        return Math.abs(a - b) <= (atol + rtol * Math.abs(b));
    });

    // Compare each element in the two sorted arrays
    for (let i = 0; i < list1.length; i++) {
        if (!customComparator(list1[i], list2[i])) {
            return false;
        }
    }

    return true;
}