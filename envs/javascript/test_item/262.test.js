class TreeNode {
  /**
   * Constructs a new TreeNode instance.
   * 
   * @param {number} val - The value of the node.
   * @param {TreeNode} [left=null] - The left child of the node.
   * @param {TreeNode} [right=null] - The right child of the node.
   */
  constructor(val = 0, left = null, right = null) {
      this.val = val;
      this.left = left;
      this.right = right;
  }
}

/**
* Calculates the average value of the nodes on each level of a binary tree.
* 
* @param {TreeNode} root - The root of the binary tree.
* @returns {number[]} An array containing the average values of each level.
*/
function averageOfLevels(root) {
  if (!root) return [];

  const averages = [];
  const queue = [root];

  while (queue.length) {
      const levelSize = queue.length;
      let sum = 0;

      for (let i = 0; i < levelSize; i++) {
          const node = queue.shift();
          sum += node.val;

          if (node.left) queue.push(node.left);
          if (node.right) queue.push(node.right);
      }

      averages.push(sum / levelSize);
  }

  return averages;
}
class TreeNode {
  /**
   * Constructs a new TreeNode instance.
   * 
   * @param {number} val - The value of the node.
   * @param {TreeNode} [left=null] - The left child of the node.
   * @param {TreeNode} [right=null] - The right child of the node.
   */
  constructor(val = 0, left = null, right = null) {
      this.val = val;
      this.left = left;
      this.right = right;
  }
}

describe('TestAverageOfLevels', () => {
  it('should handle an empty tree', () => {
      const root = null;
      const expected = [];
      expect(averageOfLevels(root)).toEqual(expected);
  });

  it('should handle a single node tree', () => {
      const root = new TreeNode(5);
      const expected = [5.0];
      expect(averageOfLevels(root)).toEqual(expected);
  });

  it('should handle a balanced tree with two levels', () => {
      const root = new TreeNode(3);
      root.left = new TreeNode(9);
      root.right = new TreeNode(20);
      const expected = [3.0, 14.5];  // Level 0: 3; Level 1: (9+20)/2 = 14.5
      expect(averageOfLevels(root)).toEqual(expected);
  });

  it('should handle an unbalanced tree', () => {
      const root = new TreeNode(1);
      root.right = new TreeNode(2);
      root.right.right = new TreeNode(3);
      const expected = [1.0, 2.0, 3.0];  // Level 0: 1; Level 1: 2; Level 2: 3
      expect(averageOfLevels(root)).toEqual(expected);
  });

  it('should handle a tree with multiple levels', () => {
      const root = new TreeNode(1);
      root.left = new TreeNode(2);
      root.right = new TreeNode(3);
      root.left.left = new TreeNode(4);
      root.left.right = new TreeNode(5);
      root.right.right = new TreeNode(8);
      const expected = [1.0, 2.5, 5.67];  // Level 0: 1; Level 1: (2+3)/2 = 2.5; Level 2: (4+5+8)/3 ≈ 5.67
      expect(averageOfLevels(root)[2]).toBeCloseTo(expected[2], 2);
      expect(averageOfLevels(root).slice(0, 2)).toEqual(expected.slice(0, 2));
  });
});
