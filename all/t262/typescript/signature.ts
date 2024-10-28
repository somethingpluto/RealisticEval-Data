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

/**
 * Given the root of a binary tree, return the average value of the nodes on each level in the form of an array.
 *
 * @param root - The root of the binary tree.
 * @returns An array containing the average values of each level.
 */
function averageOfLevels(root: TreeNode | null): number[] {}