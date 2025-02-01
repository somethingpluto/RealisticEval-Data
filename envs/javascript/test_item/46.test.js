/**
 * Binary tree node.
 */
class TreeNode {
    /**
     * Constructs a new TreeNode.
     * @param {number} [value=0] - The value of the node.
     * @param {TreeNode} [left=null] - The left child node.
     * @param {TreeNode} [right=null] - The right child node.
     */
    constructor(value = 0, left = null, right = null) {
        this.value = value;
        this.left = left;
        this.right = right;
    }
}

/**
 * Binary tree.
 */
class BinaryTree {
    /**
     * Constructs a new BinaryTree.
     * @param {TreeNode} [root=null] - The root node of the tree.
     */
    constructor(root = null) {
        this.root = root;
    }

    /**
     * Performs a preorder traversal of the tree.
     * @param {TreeNode} node - The current node being traversed.
     * @param {Array} [result=null] - The result array to store the values.
     * @returns {Array} The result array containing the values.
     */
    preorderTraversal(node, result = null) {
        if (result === null) {
            result = [];
        }
        if (node !== null) {
            result.push(node.value);
            this.preorderTraversal(node.left, result);
            this.preorderTraversal(node.right, result);
        }
        return result;
    }

    /**
     * Performs an inorder traversal of the tree.
     * @param {TreeNode} node - The current node being traversed.
     * @param {Array} [result=null] - The result array to store the values.
     * @returns {Array} The result array containing the values.
     */
    inorderTraversal(node, result = null) {
        if (result === null) {
            result = [];
        }
        if (node !== null) {
            this.inorderTraversal(node.left, result);
            result.push(node.value);
            this.inorderTraversal(node.right, result);
        }
        return result;
    }

    /**
     * Performs a postorder traversal of the tree.
     * @param {TreeNode} node - The current node being traversed.
     * @param {Array} [result=null] - The result array to store the values.
     * @returns {Array} The result array containing the values.
     */
    postorderTraversal(node, result = null) {
        if (result === null) {
            result = [];
        }
        if (node !== null) {
            this.postorderTraversal(node.left, result);
            this.postorderTraversal(node.right, result);
            result.push(node.value);
        }
        return result;
    }
}
describe('BinaryTree', () => {
  beforeEach(() => {
      // Setup basic tree structure for testing.
      // Tree structure:
      //      1
      //     / \
      //    2   3
      //   / \
      //  4   5
      this.tree = new BinaryTree(new TreeNode(1));
      this.tree.root.left = new TreeNode(2, new TreeNode(4), new TreeNode(5));
      this.tree.root.right = new TreeNode(3);

      this.emptyTree = new BinaryTree();
      this.singleNodeTree = new BinaryTree(new TreeNode(10));
  });

  describe('preorderTraversal', () => {
      it('should correctly perform preorder traversal', () => {
          const result = this.tree.preorderTraversal(this.tree.root);
          expect(result).toEqual([1, 2, 4, 5, 3]);
      });
  });

  describe('inorderTraversal', () => {
      it('should correctly perform inorder traversal', () => {
          const result = this.tree.inorderTraversal(this.tree.root);
          expect(result).toEqual([4, 2, 5, 1, 3]);
      });
  });

  describe('postorderTraversal', () => {
      it('should correctly perform postorder traversal', () => {
          const result = this.tree.postorderTraversal(this.tree.root);
          expect(result).toEqual([4, 5, 2, 3, 1]);
      });
  });

  describe('empty tree', () => {
      it('should handle an empty tree correctly', () => {
          expect(this.emptyTree.preorderTraversal(this.emptyTree.root)).toEqual([]);
          expect(this.emptyTree.inorderTraversal(this.emptyTree.root)).toEqual([]);
          expect(this.emptyTree.postorderTraversal(this.emptyTree.root)).toEqual([]);
      });
  });

  describe('single node tree', () => {
      it('should handle a single node tree correctly', () => {
          expect(this.singleNodeTree.preorderTraversal(this.singleNodeTree.root)).toEqual([10]);
          expect(this.singleNodeTree.inorderTraversal(this.singleNodeTree.root)).toEqual([10]);
          expect(this.singleNodeTree.postorderTraversal(this.singleNodeTree.root)).toEqual([10]);
      });
  });
});
