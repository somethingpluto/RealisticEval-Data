class TreeNode {
    constructor(key) {
        this.left = null;
        this.right = null;
        this.val = key;
    }
}

class BinaryTree {
    constructor() {
        this.root = null;
    }

    insert(key) {
        if (this.root === null) {
            this.root = new TreeNode(key);
        } else {
            this._insert(this.root, key);
        }
    }

    _insert(node, key) {
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

    inorderTraversal() {
        return this._inorderTraversal(this.root, []);
    }

    _inorderTraversal(node, result) {
        if (node !== null) {
            this._inorderTraversal(node.left, result);
            result.push(node.val);
            this._inorderTraversal(node.right, result);
        }
        return result;
    }

    preorderTraversal() {
        return this._preorderTraversal(this.root, []);
    }

    _preorderTraversal(node, result) {
        if (node !== null) {
            result.push(node.val);
            this._preorderTraversal(node.left, result);
            this._preorderTraversal(node.right, result);
        }
        return result;
    }

    postorderTraversal() {
        return this._postorderTraversal(this.root, []);
    }

    _postorderTraversal(node, result) {
        if (node !== null) {
            this._postorderTraversal(node.left, result);
            this._postorderTraversal(node.right, result);
            result.push(node.val);
        }
        return result;
    }
}