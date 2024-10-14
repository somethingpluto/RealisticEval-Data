// Import the function you want to test
const { areSiblings } = require('./path/to/your/function');

describe('areSiblings', () => {
  it('should return true if two values are siblings', () => {
    const tree = [3, 5, 1, 6, 2, 0, 8];
    expect(areSiblings(tree, 6, 2)).toBe(true);
  });

  it('should return false if two values are not siblings', () => {
    const tree = [3, 5, 1, 6, 2, 0, 8];
    expect(areSiblings(tree, 6, 8)).toBe(false);
  });

  it('should handle empty tree', () => {
    const tree = [];
    expect(areSiblings(tree, 1, 2)).toBe(false);
  });

  it('should handle single node tree', () => {
    const tree = [1];
    expect(areSiblings(tree, 1, 1)).toBe(false);
  });
});