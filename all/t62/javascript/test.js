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