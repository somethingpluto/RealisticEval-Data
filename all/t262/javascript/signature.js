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
function averageOfLevels(root) {}