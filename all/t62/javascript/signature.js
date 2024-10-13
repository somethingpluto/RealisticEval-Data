/**
 * Represents a node in a binary tree.
 */
class TreeNode {
    /**
     * Constructs a new TreeNode.
     * @param {number} key - The value of the node.
     */
    constructor(key) {
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
     * Constructs a new BinaryTree.
     */
    constructor() {
        this.root = null;
    }

    /**
     * Inserts a new node with the given key into the binary tree.
     * @param {number} key - The value to be inserted.
     */
    insert(key) {
        // Implementation goes here
    }

    /**
     * Inserts a new node with the given key into the subtree rooted at the specified node.
     * @param {TreeNode} node - The root node of the subtree.
     * @param {number} key - The value to be inserted.
     * @private
     */
    _insert(node, key) {
        // Implementation goes here
    }

    /**
     * Performs an in-order traversal of the binary tree.
     * @returns {Array<number>} An array containing the values of the nodes in in-order traversal order.
     */
    inorderTraversal() {
        return this._inorderTraversal(this.root, []);
    }

    /**
     * Helper method for performing an in-order traversal of the subtree rooted at the specified node.
     * @param {TreeNode} node - The root node of the subtree.
     * @param {Array<number>} result - The array to store the traversal results.
     * @returns {Array<number>} The updated result array.
     * @private
     */
    _inorderTraversal(node, result) {
        // Implementation goes here
    }

    /**
     * Performs a pre-order traversal of the binary tree.
     * @returns {Array<number>} An array containing the values of the nodes in pre-order traversal order.
     */
    preorderTraversal() {
        return this._preorderTraversal(this.root, []);
    }

    /**
     * Helper method for performing a pre-order traversal of the subtree rooted at the specified node.
     * @param {TreeNode} node - The root node of the subtree.
     * @param {Array<number>} result - The array to store the traversal results.
     * @returns {Array<number>} The updated result array.
     * @private
     */
    _preorderTraversal(node, result) {
        // Implementation goes here
    }

    /**
     * Performs a post-order traversal of the binary tree.
     * @returns {Array<number>} An array containing the values of the nodes in post-order traversal order.
     */
    postorderTraversal() {
        return this._postorderTraversal(this.root, []);
    }

    /**
     * Helper method for performing a post-order traversal of the subtree rooted at the specified node.
     * @param {TreeNode} node - The root node of the subtree.
     * @param {Array<number>} result - The array to store the traversal results.
     * @returns {Array<number>} The updated result array.
     * @private
     */
    _postorderTraversal(node, result) {
        // Implementation goes here
    }
}