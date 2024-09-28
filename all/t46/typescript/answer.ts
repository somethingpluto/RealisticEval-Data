class TreeNode {
    value: number;
    left: TreeNode | null;
    right: TreeNode | null;

    constructor(value = 0, left: TreeNode | null = null, right: TreeNode | null = null) {
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

    preorderTraversal(node: TreeNode | null, result: number[] = []): number[] {
        /** Recursive Preorder Traversal */
        if (node) {
            result.push(node.value);
            this.preorderTraversal(node.left, result);
            this.preorderTraversal(node.right, result);
        }
        return result;
    }

    inorderTraversal(node: TreeNode | null, result: number[] = []): number[] {
        /** Recursive Inorder Traversal */
        if (node) {
            this.inorderTraversal(node.left, result);
            result.push(node.value);
            this.inorderTraversal(node.right, result);
        }
        return result;
    }

    postorderTraversal(node: TreeNode | null, result: number[] = []): number[] {
        /** Recursive Postorder Traversal */
        if (node) {
            this.postorderTraversal(node.left, result);
            this.postorderTraversal(node.right, result);
            result.push(node.value);
        }
        return result;
    }

    iterativePreorder(): number[] {
        /** Iterative Preorder Traversal */
        if (!this.root) {
            return [];
        }
        
        const stack: (TreeNode | null)[] = [this.root];
        const result: number[] = [];
        
        while (stack.length) {
            const node = stack.pop()!;
            if (node) {
                result.push(node.value);
                stack.push(node.right);
                stack.push(node.left);
            }
        }
        
        return result;
    }

    iterativeInorder(): number[] {
        /** Iterative Inorder Traversal */
        const stack: TreeNode[] = [];
        const result: number[] = [];
        let current: TreeNode | null = this.root;

        while (stack.length || current) {
            while (current) {
                stack.push(current);
                current = current.left;
            }
            current = stack.pop()!;
            result.push(current.value);
            current = current.right;
        }

        return result;
    }

    iterativePostorder(): number[] {
        /** Iterative Postorder Traversal */
        if (!this.root) {
            return [];
        }
        
        const stack: TreeNode[] = [this.root];
        const result: number[] = [];
        
        while (stack.length) {
            const node = stack.pop()!;
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