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