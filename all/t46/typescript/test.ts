describe('TreeNode', () => {
    it('should create an instance of TreeNode with default values', () => {
        const node = new TreeNode();
        expect(node.value).toBe(0);
        expect(node.left).toBeNull();
        expect(node.right).toBeNull();
    });

    it('should create an instance of TreeNode with custom values', () => {
        const node = new TreeNode(5, new TreeNode(3), new TreeNode(7));
        expect(node.value).toBe(5);
        expect(node.left?.value).toBe(3);
        expect(node.right?.value).toBe(7);
    });
});

describe('BinaryTree', () => {
    it('should create an instance of BinaryTree with default root', () => {
        const tree = new BinaryTree();
        expect(tree.root).toBeNull();
    });

    it('should create an instance of BinaryTree with custom root', () => {
        const root = new TreeNode(1, new TreeNode(2), new TreeNode(3));
        const tree = new BinaryTree(root);
        expect(tree.root?.value).toBe(1);
        expect(tree.root?.left?.value).toBe(2);
        expect(tree.root?.right?.value).toBe(3);
    });

    it('should perform preorder traversal correctly', () => {
        const root = new TreeNode(1, new TreeNode(2, new TreeNode(4), new TreeNode(5)), new TreeNode(3, new TreeNode(6), new TreeNode(7)));
        const tree = new BinaryTree(root);
        const result = tree.preorderTraversal(root);
        expect(result).toEqual([1, 2, 4, 5, 3, 6, 7]);
    });

    it('should perform inorder traversal correctly', () => {
        const root = new TreeNode(1, new TreeNode(2, new TreeNode(4), new TreeNode(5)), new TreeNode(3, new TreeNode(6), new TreeNode(7)));
        const tree = new BinaryTree(root);
        const result = tree.inorderTraversal(root);
        expect(result).toEqual([4, 2, 5, 1, 6, 3, 7]);
    });

    it('should perform postorder traversal correctly', () => {
        const root = new TreeNode(1, new TreeNode(2, new TreeNode(4), new TreeNode(5)), new TreeNode(3, new TreeNode(6), new TreeNode(7)));
        const tree = new BinaryTree(root);
        const result = tree.postorderTraversal(root);
        expect(result).toEqual([4, 5, 2, 6, 7, 3, 1]);
    });
});