describe('BinaryTree', () => {
    let binaryTree;

    beforeEach(() => {
        binaryTree = new BinaryTree();
    });

    it('should insert nodes correctly', () => {
        binaryTree.insert(10);
        binaryTree.insert(5);
        binaryTree.insert(15);
        binaryTree.insert(3);
        binaryTree.insert(7);

        expect(binaryTree.inorderTraversal()).toEqual([3, 5, 7, 10, 15]);
        expect(binaryTree.preorderTraversal()).toEqual([10, 5, 3, 7, 15]);
        expect(binaryTree.postorderTraversal()).toEqual([3, 7, 5, 15, 10]);
    });
});