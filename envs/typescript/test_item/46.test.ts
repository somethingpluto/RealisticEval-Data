// Assuming the TreeNode class is already defined above

/**
 * Represents a binary tree.
 */
class BinaryTree {
    root: TreeNode | null;

    constructor(root: TreeNode | null = null) {
        this.root = root;
    }

    /**
     * Performs a recursive preorder traversal.
     * @param node The current node being traversed.
     * @param result The array to store the traversal results.
     * @returns An array containing the preorder traversal results.
     */
    preorderTraversal(node: TreeNode | null, result: number[] = []): number[] {
        if (node) {
            result.push(node.value);
            this.preorderTraversal(node.left, result);
            this.preorderTraversal(node.right, result);
        }
        return result;
    }

    /**
     * Performs a recursive inorder traversal.
     * @param node The current node being traversed.
     * @param result The array to store the traversal results.
     * @returns An array containing the inorder traversal results.
     */
    inorderTraversal(node: TreeNode | null, result: number[] = []): number[] {
        if (node) {
            this.inorderTraversal(node.left, result);
            result.push(node.value);
            this.inorderTraversal(node.right, result);
        }
        return result;
    }

    /**
     * Performs a recursive postorder traversal.
     * @param node The current node being traversed.
     * @param result The array to store the traversal results.
     * @returns An array containing the postorder traversal results.
     */
    postorderTraversal(node: TreeNode | null, result: number[] = []): number[] {
        if (node) {
            this.postorderTraversal(node.left, result);
            this.postorderTraversal(node.right, result);
            result.push(node.value);
        }
        return result;
    }
}
describe('BinaryTree', () => {
    let tree: BinaryTree;

    beforeEach(() => {
        // Setup basic tree structure for testing.
        // Tree structure:
        //      1
        //     / \
        //    2   3
        //   / \
        //  4   5
        tree = new BinaryTree(new TreeNode(1));
        tree.root.left = new TreeNode(2, new TreeNode(4), new TreeNode(5));
        tree.root.right = new TreeNode(3);
    });

    describe('preorderTraversal', () => {
        it('should perform preorder traversal correctly', () => {
            const result = tree.preorderTraversal(tree.root);
            expect(result).toEqual([1, 2, 4, 5, 3]);
        });
    });

    describe('inorderTraversal', () => {
        it('should perform inorder traversal correctly', () => {
            const result = tree.inorderTraversal(tree.root);
            expect(result).toEqual([4, 2, 5, 1, 3]);
        });
    });

    describe('postorderTraversal', () => {
        it('should perform postorder traversal correctly', () => {
            const result = tree.postorderTraversal(tree.root);
            expect(result).toEqual([4, 5, 2, 3, 1]);
        });
    });

    describe('empty tree', () => {
        it('should handle an empty tree correctly', () => {
            const emptyTree = new BinaryTree();
            expect(emptyTree.preorderTraversal(emptyTree.root)).toEqual([]);
            expect(emptyTree.inorderTraversal(emptyTree.root)).toEqual([]);
            expect(emptyTree.postorderTraversal(emptyTree.root)).toEqual([]);
        });
    });

    describe('single node tree', () => {
        it('should handle a single node tree correctly', () => {
            const singleNodeTree = new BinaryTree(new TreeNode(10));
            expect(singleNodeTree.preorderTraversal(singleNodeTree.root)).toEqual([10]);
            expect(singleNodeTree.inorderTraversal(singleNodeTree.root)).toEqual([10]);
            expect(singleNodeTree.postorderTraversal(singleNodeTree.root)).toEqual([10]);
        });
    });
});
