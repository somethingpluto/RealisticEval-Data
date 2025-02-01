/**
 * Determines if two values are siblings in a binary tree represented as an array.
 *
 * @param {Array<number>} tree - the binary tree level-order representation
 * @param {number} val1 - the first value to check for sibling relationship
 * @param {number} val2 - the second value to check for sibling relationship
 * @returns {boolean} - true if val1 and val2 are siblings, false otherwise
 */
function areSiblings(tree, val1, val2) {
    if (tree.length < 2) {
        return false;
    }

    for (let i = 0; i < tree.length; i += 2) {
        if ((tree[i] === val1 && tree[i + 1] === val2) || (tree[i] === val2 && tree[i + 1] === val1)) {
            return true;
        }
    }

    return false;
}
describe('TestAreSiblings', () => {
  let tree;

  beforeEach(() => {
      // Setting up a binary tree used for all the test cases
      tree = [1, 2, 3, 4, 5, 6, 7];
  });

  it('test with nodes 4 and 5, which are siblings', () => {
      const result = areSiblings(tree, 4, 5);
      expect(result).toBe(true);
  });

  it('test with nodes 4 and 6, which are not siblings', () => {
      const result = areSiblings(tree, 4, 6);
      expect(result).toBe(false);
  });

  it('test with node 1 (root) and any other node, should return false', () => {
      const result = areSiblings(tree, 1, 2);
      expect(result).toBe(false);
  });

  it('test with non-existent values', () => {
      const result = areSiblings(tree, 8, 9);
      expect(result).toBe(false);
  });

  it('test with the same node for both values', () => {
      const result = areSiblings(tree, 4, 4);
      expect(result).toBe(false);
  });
});
