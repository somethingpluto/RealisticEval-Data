class TreeNode {
    value: number;
    left: TreeNode | null;
    right: TreeNode | null;

    constructor(value: number = 0, left: TreeNode | null = null, right: TreeNode | null = null) {
        this.value = value;
        this.left = left;
        this.right = right;
    }
}

class BinaryTree {
    root: TreeNode | null;

    constructor(root: TreeNode | null = null) {
        this.root = root;
    }

    preorderTraversal(node: TreeNode | null, result?: number[]): number[] {
        if (result === undefined) {
            result = [];
        }
        if (node !== null) {
            result.push(node.value);
            this.preorderTraversal(node.left, result);
            this.preorderTraversal(node.right, result);
        }
        return result;
    }

    inorderTraversal(node: TreeNode | null, result?: number[]): number[] {
        if (result === undefined) {
            result = [];
        }
        if (node !== null) {
            this.inorderTraversal(node.left, result);
            result.push(node.value);
            this.inorderTraversal(node.right, result);
        }
        return result;
    }

    postorderTraversal(node: TreeNode | null, result?: number[]): number[] {
        if (result === undefined) {
            result = [];
        }
        if (node !== null) {
            this.postorderTraversal(node.left, result);
            this.postorderTraversal(node.right, result);
            result.push(node.value);
        }
        return result;
    }

    iterativePreorder(): number[] {
        if (!this.root) {
            return [];
        }
        let stack: TreeNode[] = [this.root];
        let result: number[] = [];
        while (stack.length > 0) {
            const node = stack.pop();
            if (node) {
                result.push(node.value);
                if (node.right) {
                    stack.push(node.right);
                }
                if (node.left) {
                    stack.push(node.left);
                }
            }
        }
        return result;
    }

    iterativeInorder(): number[] {
        let stack: TreeNode[] = [];
        let result: number[] = [];
        let current: TreeNode | null = this.root;
        while (stack.length > 0 || current !== null) {
            while (current) {
                stack.push(current);
                current = current.left;
            }
            current = stack.pop();
            if (current) {
                result.push(current.value);
                current = current.right;
            }
        }
        return result;
    }

    iterativePostorder(): number[] {
        if (!this.root) {
            return [];
        }
        let stack: TreeNode[] = [this.root];
        let result: number[] = [];
        while (stack.length > 0) {
            const node = stack.pop();
            if (node) {
                result.unshift(node.value);
                if (node.left) {
                    stack.push(node.left);
                }
                if (node.right) {
                    stack.push(node.right);
                }
            }
        }
        return result;
    }
}