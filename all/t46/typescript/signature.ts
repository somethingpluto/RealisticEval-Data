/**
 * Represents a binary tree node.
 */
class TreeNode {
    value: number;
    left: TreeNode | null;
    right: TreeNode | null;

    /**
     * Constructs a new TreeNode.
     * @param value The value of the node.
     * @param left The left child of the node.
     * @param right The right child of the node.
     */
    constructor(value: number = 0, left: TreeNode | null = null, right: TreeNode | null = null) {
        this.value = value;
        this.left = left;
        this.right = right;
    }
}

/**
 * Represents a binary tree.
 */
class BinaryTree {
    root: TreeNode | null;

    /**
     * Constructs a new BinaryTree.
     * @param root The root node of the binary tree.
     */
    constructor(root: TreeNode | null = null) {
        this.root = root;
    }

    /**
     * Performs a recursive preorder traversal.
     * @param node The current node being traversed.
     * @param result The array to store the traversal results.
     * @returns An array containing the preorder traversal results.
     */
    preorderTraversal(node: TreeNode | null, result?: number[]): number[] {
    }

    /**
     * Performs a recursive inorder traversal.
     * @param node The current node being traversed.
     * @param result The array to store the traversal results.
     * @returns An array containing the inorder traversal results.
     */
    inorderTraversal(node: TreeNode | null, result?: number[]): number[] {
    }

    /**
     * Performs a recursive postorder traversal.
     * @param node The current node being traversed.
     * @param result The array to store the traversal results.
     * @returns An array containing the postorder traversal results.
     */
    postorderTraversal(node: TreeNode | null, result?: number[]): number[] {
    }
}