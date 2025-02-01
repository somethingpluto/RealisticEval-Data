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
        if (this.root === null) {
            this.root = new TreeNode(key);
        } else {
            this._insert(this.root, key);
        }
    }

    /**
     * Inserts a new node with the given key into the subtree rooted at the specified node.
     * @param {TreeNode} node - The root node of the subtree.
     * @param {number} key - The value to be inserted.
     * @private
     */
    _insert(node, key) {
        if (key < node.val) {
            if (node.left === null) {
                node.left = new TreeNode(key);
            } else {
                this._insert(node.left, key);
            }
        } else {
            if (node.right === null) {
                node.right = new TreeNode(key);
            } else {
                this._insert(node.right, key);
            }
        }
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
        if (node !== null) {
            this._inorderTraversal(node.left, result);
            result.push(node.val);
            this._inorderTraversal(node.right, result);
        }
        return result;
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
        if (node !== null) {
            result.push(node.val);
            this._preorderTraversal(node.left, result);
            this._preorderTraversal(node.right, result);
        }
        return result;
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
        if (node !== null) {
            this._postorderTraversal(node.left, result);
            this._postorderTraversal(node.right, result);
            result.push(node.val);
        }
        return result;
    }
}
describe('BinaryTree', () => {
    describe('test_empty_tree', () => {
        it('should handle an empty tree correctly', () => {
            const bt = new BinaryTree();
            expect(bt.inorderTraversal()).toEqual([]);
            expect(bt.preorderTraversal()).toEqual([]);
            expect(bt.postorderTraversal()).toEqual([]);
        });
    });

    describe('test_single_node_tree', () => {
        it('should handle a single node tree correctly', () => {
            const bt = new BinaryTree();
            bt.insert(10);
            expect(bt.inorderTraversal()).toEqual([10]);
            expect(bt.preorderTraversal()).toEqual([10]);
            expect(bt.postorderTraversal()).toEqual([10]);
        });
    });

    describe('test_balanced_tree', () => {
        it('should handle a balanced tree correctly', () => {
            const bt = new BinaryTree();
            const elements = [8, 3, 10, 1, 6, 9, 14];
            elements.forEach((elem) => bt.insert(elem));
            expect(bt.inorderTraversal()).toEqual([1, 3, 6, 8, 9, 10, 14]);
            expect(bt.preorderTraversal()).toEqual([8, 3, 1, 6, 10, 9, 14]);
            expect(bt.postorderTraversal()).toEqual([1, 6, 3, 9, 14, 10, 8]);
        });
    });

    describe('test_left_heavy_tree', () => {
        it('should handle a left-heavy tree correctly', () => {
            const bt = new BinaryTree();
            for (let i = 10; i > 0; i--) {
                bt.insert(i);
            }
            expect(bt.inorderTraversal()).toEqual([...Array(10).keys()].map(i => i + 1));
            expect(bt.preorderTraversal()).toEqual([...Array(10).keys()].map(i => 10 - i));
            expect(bt.postorderTraversal()).toEqual([...Array(10).keys()].map(i => i + 1));
        });
    });

    describe('test_right_heavy_tree', () => {
        it('should handle a right-heavy tree correctly', () => {
            const bt = new BinaryTree();
            for (let i = 1; i <= 10; i++) {
                bt.insert(i);
            }
            expect(bt.inorderTraversal()).toEqual([...Array(10).keys()].map(i => i + 1));
            expect(bt.preorderTraversal()).toEqual([...Array(10).keys()].map(i => i + 1));
            expect(bt.postorderTraversal()).toEqual([...Array(10).keys()].reverse().map(i => i + 1));
        });
    });
});
