class TreeNode {
  constructor(val = 0, left = null, right = null) {
      this.val = val;
      this.left = left;
      this.right = right;
  }
}

function averageOfLevels(root) {
  /**
   * Given the root of a binary tree, return the average value of the nodes on each level in the form of an array.
   *
   * @param {TreeNode} root - The root of the binary tree.
   * @returns {number[]} - An array containing the average values of each level.
   */
  if (!root) {
      return [];
  }

  let result = [];
  let queue = [[root, 0]];  // [node, level]

  while (queue.length > 0) {
      let currentLevel = [];
      let levelSize = queue.length;

      for (let i = 0; i < levelSize; i++) {
          let [node, level] = queue.shift();
          currentLevel.push(node.val);

          if (node.left) {
              queue.push([node.left, level + 1]);
          }
          if (node.right) {
              queue.push([node.right, level + 1]);
          }
      }

      // Calculate the average for the current level
      let levelAverage = currentLevel.reduce((acc, val) => acc + val, 0) / currentLevel.length;
      result.push(levelAverage);
  }

  return result;
}