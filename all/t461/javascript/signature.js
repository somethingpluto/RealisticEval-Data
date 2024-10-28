class TreeNode {
    /** 
     * Definition for a binary tree node. 
     * @param {number} val 
     * @param {TreeNode|null} left 
     * @param {TreeNode|null} right 
     */
    constructor(val = 0, left = null, right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

/**
 * Calculate the average value of nodes at each level of a binary tree.
 * 
 * @param {TreeNode|null} root - The root of the binary tree.
 * @returns {number[]} A list of averages for each level of the binary tree.
 */
function averageOfLevels(root) {}