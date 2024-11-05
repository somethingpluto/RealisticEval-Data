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

function averageOfLevels(root: TreeNode | null): number[] {
  if (!root) {
      return [];
  }

  const result: number[] = [];
  let queue: [TreeNode, number][] = [[root, 0]]; // (node, level)

  while (queue.length > 0) {
      const currentLevelValues: number[] = [];
      const levelSize = queue.length;

      for (let i = 0; i < levelSize; i++) {
          const [node, level] = queue.shift()!;
          currentLevelValues.push(node.val);

          if (node.left) {
              queue.push([node.left, level + 1]);
          }
          if (node.right) {
              queue.push([node.right, level + 1]);
          }
      }

      // Calculate the average for the current level
      const levelAverage = currentLevelValues.reduce((acc, val) => acc + val, 0) / currentLevelValues.length;
      result.push(levelAverage);
  }

  return result;
}