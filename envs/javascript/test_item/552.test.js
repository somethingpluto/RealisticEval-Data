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
    if (set1.size !== set2.size) {
        return false;
    }

    for (let value of set1) {
        let found = false;
        for (let otherValue of set2) {
            if (Math.abs(value - otherValue) <= atol + rtol * Math.abs(otherValue)) {
                found = true;
                break;
            }
        }
        if (!found) {
            return false;
        }
    }

    return true;
}
describe('TestAreSetsEqual', () => {

    describe('test_identical_sets', () => {
        it('should return true for two identical sets of floats', () => {
            const set1 = new Set([1.0, 2.0, 3.0]);
            const set2 = new Set([1.0, 2.0, 3.0]);
            expect(areSetsEqual(set1, set2)).toBe(true);
        });
    });

    describe('test_sets_with_close_values', () => {
        it('should return true for two sets that are close within the tolerance', () => {
            const set1 = new Set([1.0, 2.00001, 3.0]);
            const set2 = new Set([1.0, 2.00002, 3.0]);
            expect(areSetsEqual(set1, set2, 1e-5, 1e-6)).toBe(true);
        });
    });

    describe('test_sets_with_large_difference', () => {
        it('should return false for two sets that have large differences beyond tolerance', () => {
            const set1 = new Set([1.0, 2.0, 3.0]);
            const set2 = new Set([1.0, 2.5, 3.0]);
            expect(areSetsEqual(set1, set2)).toBe(false);
        });
    });

    describe('test_sets_with_one_different_values', () => {
        it('should return true for two sets containing one different float', () => {
            const set1 = new Set([1.0, 2.0, 3.0]);
            const set2 = new Set([1.0, 2.000001, 3.0]);
            expect(areSetsEqual(set1, set2, 1e-5, 1e-6)).toBe(true);
        });
    });

    describe('test_empty_sets', () => {
        it('should return true for two empty sets', () => {
            const set1 = new Set();
            const set2 = new Set();
            expect(areSetsEqual(set1, set2)).toBe(true);
        });
    });

});
