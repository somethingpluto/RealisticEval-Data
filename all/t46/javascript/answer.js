class TreeNode {
    constructor(value = 0, left = null, right = null) {
        this.value = value;
        this.left = left;
        this.right = right;
    }
}

class BinaryTree {
    constructor(root = null) {
        this.root = root;
    }

    preorderTraversal(node, result = null) {
        if (result === null) {
            result = [];
        }
        if (node) {
            result.push(node.value);
            this.preorderTraversal(node.left, result);
            this.preorderTraversal(node.right, result);
        }
        return result;
    }

    inorderTraversal(node, result = null) {
        if (result === null) {
            result = [];
        }
        if (node) {
            this.inorderTraversal(node.left, result);
            result.push(node.value);
            this.inorderTraversal(node.right, result);
        }
        return result;
    }

    postorderTraversal(node, result = null) {
        if (result === null) {
            result = [];
        }
        if (node) {
            this.postorderTraversal(node.left, result);
            this.postorderTraversal(node.right, result);
            result.push(node.value);
        }
        return result;
    }

    iterativePreorder() {
        if (!this.root) {
            return [];
        }
        let stack = [this.root];
        let result = [];
        while (stack.length > 0) {
            let node = stack.pop();
            if (node) {
                result.push(node.value);
                stack.push(node.right);
                stack.push(node.left);
            }
        }
        return result;
    }

    iterativeInorder() {
        let stack = [];
        let result = [];
        let current = this.root;
        while (stack.length > 0 || current) {
            while (current) {
                stack.push(current);
                current = current.left;
            }
            current = stack.pop();
            result.push(current.value);
            current = current.right;
        }
        return result;
    }

    iterativePostorder() {
        if (!this.root) {
            return [];
        }
        let stack = [this.root];
        let result = [];
        while (stack.length > 0) {
            let node = stack.pop();
            result.unshift(node.value);
            if (node.left) {
                stack.push(node.left);
            }
            if (node.right) {
                stack.push(node.right);
            }
        }
        return result;
    }
}