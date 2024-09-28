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

    preorderTraversal(node, result = []) {
        if (node !== null) {
            result.push(node.value);
            this.preorderTraversal(node.left, result);
            this.preorderTraversal(node.right, result);
        }
        return result;
    }

    inorderTraversal(node, result = []) {
        if (node !== null) {
            this.inorderTraversal(node.left, result);
            result.push(node.value);
            this.inorderTraversal(node.right, result);
        }
        return result;
    }

    postorderTraversal(node, result = []) {
        if (node !== null) {
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
        const stack = [this.root];
        const result = [];
        while (stack.length > 0) {
            const node = stack.pop();
            if (node !== null) {
                result.push(node.value);
                if (node.right !== null) stack.push(node.right);
                if (node.left !== null) stack.push(node.left);
            }
        }
        return result;
    }

    iterativeInorder() {
        const stack = [];
        const result = [];
        let current = this.root;
        while (stack.length > 0 || current !== null) {
            while (current !== null) {
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
        const stack = [this.root];
        const result = [];
        while (stack.length > 0) {
            const node = stack.pop();
            result.unshift(node.value);
            if (node.left !== null) stack.push(node.left);
            if (node.right !== null) stack.push(node.right);
        }
        return result;
    }
}