class TreeNode {
    left: TreeNode | null;
    right: TreeNode | null;
    val: number;

    constructor(key: number) {
        this.left = null;
        this.right = null;
        this.val = key;
    }
}

class BinaryTree {
    root: TreeNode | null;

    constructor() {
        this.root = null;
    }

    insert(key: number): void {
        if (this.root === null) {
            this.root = new TreeNode(key);
        } else {
            this._insert(this.root, key);
        }
    }

    private _insert(node: TreeNode, key: number): void {
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