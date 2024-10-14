import { describe, it, expect } from '@jest/globals';

// Assuming the function areSiblings is defined somewhere in your project
function areSiblings(tree: number[], val1: number, val2: number): boolean {
    // Implementation of the function goes here
    const index1 = tree.indexOf(val1);
    const index2 = tree.indexOf(val2);

    if (index1 === -1 || index2 === -1) return false;

    const parentIndex1 = Math.floor((index1 - 1) / 2);
    const parentIndex2 = Math.floor((index2 - 1) / 2);

    return parentIndex1 === parentIndex2;
}

describe('areSiblings', () => {
    it('should return true if val1 and val2 are siblings', () => {
        const tree = [3, 5, 1, 6, 2, 0, 8];
        expect(areSiblings(tree, 5, 1)).toBe(true);
    });

    it('should return false if val1 and val2 are not siblings', () => {
        const tree = [3, 5, 1, 6, 2, 0, 8];
        expect(areSiblings(tree, 5, 8)).toBe(false);
    });

    it('should return false if one or both values are not in the tree', () => {
        const tree = [3, 5, 1, 6, 2, 0, 8];
        expect(areSiblings(tree, 9, 1)).toBe(false);
        expect(areSiblings(tree, 5, 10)).toBe(false);
        expect(areSiblings(tree, 9, 10)).toBe(false);
    });
});
