/**
 * Represents a node in a binary tree.
 */
class TreeNode {
    left: TreeNode | null;
    right: TreeNode | null;
    val: number;

    constructor(key: number) {
        this.left = null;
        this.right = null;
        this.val = key;
    }
}

/**
 * Represents a binary tree and implements its traversal methods.
 */
class BinaryTree {
    /**
     * Initializes a new instance of the BinaryTree class.
     */
    root: TreeNode | null;

    constructor() {
        this.root = null;
    }

    /**
     * Inserts a new node with the given key into the binary tree.
     * @param key The value to insert.
     */
    insert(key: number): void {
    }

    /**
     * Helper method to insert a new node with the given key into the binary tree.
     * @param node The current node.
     * @param key The value to insert.
     */
    private _insert(node: TreeNode, key: number): void {
    }

    /**
     * Performs an in-order traversal of the binary tree.
     * @returns An array containing the values of the nodes in in-order traversal order.
     */
    inorderTraversal(): number[] {
    }

    /**
     * Helper method to perform an in-order traversal of the binary tree.
     * @param node The current node.
     * @param result The array to store the traversal results.
     */
    private _inorderTraversal(node: TreeNode | null, result: number[]): void {
    }

    /**
     * Performs a pre-order traversal of the binary tree.
     * @returns An array containing the values of the nodes in pre-order traversal order.
     */
    preorderTraversal(): number[] {
    }

    /**
     * Helper method to perform a pre-order traversal of the binary tree.
     * @param node The current node.
     * @param result The array to store the traversal results.
     */
    private _preorderTraversal(node: TreeNode | null, result: number[]): void {
    }

    /**
     * Performs a post-order traversal of the binary tree.
     * @returns An array containing the values of the nodes in post-order traversal order.
     */
    postorderTraversal(): number[] {
    }

    /**
     * Helper method to perform a post-order traversal of the binary tree.
     * @param node The current node.
     * @param result The array to store the traversal results.
     */
    private _postorderTraversal(node: TreeNode | null, result: number[]): void {
    }
}