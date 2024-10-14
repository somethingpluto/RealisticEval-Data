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