class BinaryTree {
    root: TreeNode | null;

    constructor() {
        this.root = null;
    }

    insert(key: number): void {
        this.root = this._insert(this.root, key);
    }

    private _insert(node: TreeNode | null, key: number): TreeNode {
        if (node === null) {
            return new TreeNode(key);
        }

        if (key < node.val) {
            node.left = this._insert(node.left, key);
        } else if (key > node.val) {
            node.right = this._insert(node.right, key);
        }

        return node;
    }

    inorderTraversal(): number[] {
        const result: number[] = [];
        this._inorderTraversal(this.root, result);
        return result;
    }

    private _inorderTraversal(node: TreeNode | null, result: number[]): void {
        if (node !== null) {
            this._inorderTraversal(node.left, result);
            result.push(node.val);
            this._inorderTraversal(node.right, result);
        }
    }

    preorderTraversal(): number[] {
        const result: number[] = [];
        this._preorderTraversal(this.root, result);
        return result;
    }

    private _preorderTraversal(node: TreeNode | null, result: number[]): void {
        if (node !== null) {
            result.push(node.val);
            this._preorderTraversal(node.left, result);
            this._preorderTraversal(node.right, result);
        }
    }

    postorderTraversal(): number[] {
        const result: number[] = [];
        this._postorderTraversal(this.root, result);
        return result;
    }

    private _postorderTraversal(node: TreeNode | null, result: number[]): void {
        if (node !== null) {
            this._postorderTraversal(node.left, result);
            this._postorderTraversal(node.right, result);
            result.push(node.val);
        }
    }
}
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
