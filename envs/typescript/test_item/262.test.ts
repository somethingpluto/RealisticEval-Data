function averageOfLevels(root: TreeNode | null): number[] {
    if (!root) return [];

    const result: number[] = [];
    const queue: TreeNode[] = [root];

    while (queue.length > 0) {
        let levelSum = 0;
        const levelSize = queue.length;

        for (let i = 0; i < levelSize; i++) {
            const currentNode = queue.shift()!;
            levelSum += currentNode.val;

            if (currentNode.left) queue.push(currentNode.left);
            if (currentNode.right) queue.push(currentNode.right);
        }

        result.push(levelSum / levelSize);
    }

    return result;
}
class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;

  constructor(val: number = 0, left: TreeNode | null = null, right: TreeNode | null = null) {
      this.val = val;
      this.left = left;
      this.right = right;
  }
}
describe('averageOfLevels', () => {
  it('should handle an empty tree', () => {
      const root = null;
      const expected = [];
      expect(averageOfLevels(root)).toEqual(expected);
  });

  it('should handle a single-node tree', () => {
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


