// ... (previous code for context)
import { isEqual } from 'lodash';

function areSetsEqual(set1: Set<number>, set2: Set<number>, rtol: number = 1e-5, atol: number = 1e-6): boolean {
  if (set1.size !== set2.size) return false;

  const sortedSet1 = Array.from(set1).sort((a, b) => a - b);
  const sortedSet2 = Array.from(set2).sort((a, b) => a - b);

  for (let i = 0; i < sortedSet1.length; i++) {
    if (!isEqual(sortedSet1[i], sortedSet2[i], rtol, atol)) {
      return false;
    }
  }

  return true;
}
// ... (continuation of the code)
describe('areSetsEqual', () => {
    describe('with identical sets', () => {
        it('should return true for two identical sets of floats', () => {
            const set1 = new Set([1.0, 2.0, 3.0]);
            const set2 = new Set([1.0, 2.0, 3.0]);
            expect(areSetsEqual(set1, set2)).toBe(true);
        });
    });

    describe('with sets that are close within the tolerance', () => {
        it('should return true for two sets that are close within the tolerance', () => {
            const set1 = new Set([1.0, 2.00001, 3.0]);
            const set2 = new Set([1.0, 2.00002, 3.0]);
            expect(areSetsEqual(set1, set2, 1e-5, 1e-6)).toBe(true);
        });
    });

    describe('with sets that have large differences beyond tolerance', () => {
        it('should return false for two sets that have large differences beyond tolerance', () => {
            const set1 = new Set([1.0, 2.0, 3.0]);
            const set2 = new Set([1.0, 2.5, 3.0]);
            expect(areSetsEqual(set1, set2)).toBe(false);
        });
    });

    describe('with sets containing one different float', () => {
        it('should return true for two sets containing one different float within tolerance', () => {
            const set1 = new Set([1.0, 2.0, 3.0]);
            const set2 = new Set([1.0, 2.000001, 3.0]);
            expect(areSetsEqual(set1, set2, 1e-5, 1e-6)).toBe(true);
        });
    });

    describe('with empty sets', () => {
        it('should return true for two empty sets', () => {
            const set1 = new Set<number>();
            const set2 = new Set<number>();
            expect(areSetsEqual(set1, set2)).toBe(true);
        });
    });
});
