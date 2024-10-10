describe('BinaryTree', () => {
    let binaryTree;
  
    beforeEach(() => {
      binaryTree = new BinaryTree();
    });
  
    describe('#preorderTraversal', () => {
      it('should return an empty array when called with no node', () => {
        const result = binaryTree.preorderTraversal(null);
        expect(result).toEqual([]);
      });
    });
  
    describe('#inorderTraversal', () => {
      it('should return an empty array when called with no node', () => {
        const result = binaryTree.inorderTraversal(null);
        expect(result).toEqual([]);
      });
    });
  
    describe('#postorderTraversal', () => {
      it('should return an empty array when called with no node', () => {
        const result = binaryTree.postorderTraversal(null);
        expect(result).toEqual([]);
      });
    });
  });