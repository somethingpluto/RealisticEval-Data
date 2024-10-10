describe('BinaryTree', () => {
  let binaryTree: BinaryTree;

  beforeEach(() => {
    binaryTree = new BinaryTree();
  });

  describe('insert method', () => {
    it('should insert a node correctly', () => {
      binaryTree.insert(10);
      expect(binaryTree.root).not.toBeNull();
      expect(binaryTree.root.val).toBe(10);
    });

    it('should insert nodes correctly with left and right children', () => {
      binaryTree.insert(10);
      binaryTree.insert(5);
      binaryTree.insert(15);

      expect(binaryTree.root.val).toBe(10);
      expect(binaryTree.root.left.val).toBe(5);
      expect(binaryTree.root.right.val).toBe(15);
    });
  });

  describe('inorder traversal', () => {
    it('should return correct inorder traversal for an empty tree', () => {
      const result: number[] = [];
      binaryTree.inorderTraversal(result);
      expect(result).toEqual([]);
    });

    it('should return correct inorder traversal for a single node', () => {
      binaryTree.insert(10);
      const result: number[] = [];
      binaryTree.inorderTraversal(result);
      expect(result).toEqual([10]);
    });

    it('should return correct inorder traversal for multiple nodes', () => {
      binaryTree.insert(10);
      binaryTree.insert(5);
      binaryTree.insert(15);
      binaryTree.insert(3);
      binaryTree.insert(7);
      binaryTree.insert(12);
      binaryTree.insert(18);

      const result: number[] = [];
      binaryTree.inorderTraversal(result);
      expect(result).toEqual([3, 5, 7, 10, 12, 15, 18]);
    });
  });

  describe('preorder traversal', () => {
    it('should return correct preorder traversal for an empty tree', () => {
      const result: number[] = [];
      binaryTree.preorderTraversal(result);
      expect(result).toEqual([]);
    });

    it('should return correct preorder traversal for a single node', () => {
      binaryTree.insert(10);
      const result: number[] = [];
      binaryTree.preorderTraversal(result);
      expect(result).toEqual([10]);
    });

    it('should return correct preorder traversal for multiple nodes', () => {
      binaryTree.insert(10);
      binaryTree.insert(5);
      binaryTree.insert(15);
      binaryTree.insert(3);
      binaryTree.insert(7);
      binaryTree.insert(12);
      binaryTree.insert(18);

      const result: number[] = [];
      binaryTree.preorderTraversal(result);
      expect(result).toEqual([10, 5, 3, 7, 15, 12, 18]);
    });
  });

  describe('postorder traversal', () => {
    it('should return correct postorder traversal for an empty tree', () => {
      const result: number[] = [];
      binaryTree.postorderTraversal(result);
      expect(result).toEqual([]);
    });

    it('should return correct postorder traversal for a single node', () => {
      binaryTree.insert(10);
      const result: number[] = [];
      binaryTree.postorderTraversal(result);
      expect(result).toEqual([10]);
    });

    it('should return correct postorder traversal for multiple nodes', () => {
      binaryTree.insert(10);
      binaryTree.insert(5);
      binaryTree.insert(15);
      binaryTree.insert(3);
      binaryTree.insert(7);
      binaryTree.insert(12);
      binaryTree.insert(18);

      const result: number[] = [];
      binaryTree.postorderTraversal(result);
      expect(result).toEqual([3, 7, 5, 12, 18, 15, 10]);
    });
  });
});