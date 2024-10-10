/**
 * Binary Tree Node
 */
class TreeNode {
    /**
     * Value of the node.
     */
    value: number;

    /**
     * Left child of the node.
     */
    left: TreeNode | null;

    /**
     * Right child of the node.
     */
    right: TreeNode | null;

    constructor(value: number = 0, left: TreeNode | null = null, right: TreeNode | null = null) {
        this.value = value;
        this.left = left;
        this.right = right;
    }
}

/**
 * Binary Tree
 */
class BinaryTree {
    /**
     * Root of the binary tree.
     */
    root: TreeNode | null;

    constructor(root: TreeNode | null = null) {
        this.root = root;
    }

    /**
     * Perform Pre-Order Traversal on the binary tree.
     * @param node - The current node being visited.
     * @param result - Array to store traversal results.
     */
    preorderTraversal(node: TreeNode | null, result: number[] = []): number[] {
        // Implementation goes here
        return result;
    }

    /**
     * Perform In-Order Traversal on the binary tree.
     * @param node - The current node being visited.
     * @param result - Array to store traversal results.
     */
    inorderTraversal(node: TreeNode | null, result: number[] = []): number[] {
        // Implementation goes here
        return result;
    }

    /**
     * Perform Post-Order Traversal on the binary tree.
     * @param node - The current node being visited.
     * @param result - Array to store traversal results.
     */
    postorderTraversal(node: TreeNode | null, result: number[] = []): number[] {
        // Implementation goes here
        return result;
    }
}