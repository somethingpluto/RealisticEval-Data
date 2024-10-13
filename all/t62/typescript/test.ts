describe('BinaryTree', () => {
  it('should handle an empty tree', () => {
      const bt = new BinaryTree();
      expect(bt.inorderTraversal()).toEqual([]);
      expect(bt.preorderTraversal()).toEqual([]);
      expect(bt.postorderTraversal()).toEqual([]);
  });

  it('should handle a single node tree', () => {
      const bt = new BinaryTree();
      bt.insert(10);
      expect(bt.inorderTraversal()).toEqual([10]);
      expect(bt.preorderTraversal()).toEqual([10]);
      expect(bt.postorderTraversal()).toEqual([10]);
  });

  it('should handle a balanced tree', () => {
      const bt = new BinaryTree();
      const elements = [8, 3, 10, 1, 6, 9, 14];
      elements.forEach((elem) => bt.insert(elem));
      expect(bt.inorderTraversal()).toEqual([1, 3, 6, 8, 9, 10, 14]);
      expect(bt.preorderTraversal()).toEqual([8, 3, 1, 6, 10, 9, 14]);
      expect(bt.postorderTraversal()).toEqual([1, 6, 3, 9, 14, 10, 8]);
  });

  it('should handle a left-heavy tree', () => {
      const bt = new BinaryTree();
      for (let i = 10; i >= 1; i--) {
          bt.insert(i);
      }
      expect(bt.inorderTraversal()).toEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
      expect(bt.preorderTraversal()).toEqual([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]);
      expect(bt.postorderTraversal()).toEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
  });

  it('should handle a right-heavy tree', () => {
      const bt = new BinaryTree();
      for (let i = 1; i <= 10; i++) {
          bt.insert(i);
      }
      expect(bt.inorderTraversal()).toEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
      expect(bt.preorderTraversal()).toEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
      expect(bt.postorderTraversal()).toEqual([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]);
  });
});