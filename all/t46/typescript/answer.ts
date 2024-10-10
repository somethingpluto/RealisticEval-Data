interface TreeNode {
    value: number;
    left?: TreeNode;
    right?: TreeNode;
}

// Define the BinaryTree class
class BinaryTree {
    private root?: TreeNode;

    constructor(root?: TreeNode) {
        this.root = root;
    }

    // Pre-order traversal method
    public preorderTraversal(node: TreeNode | undefined, result: number[] = []): number[] {
        if (node) {
            result.push(node.value);
            this.preorderTraversal(node.left, result);
            this.preorderTraversal(node.right, result);
        }
        return result;
    }

    // In-order traversal method
    public inorderTraversal(node: TreeNode | undefined, result: number[] = []): number[] {
        if (node) {
            this.inorderTraversal(node.left, result);
            result.push(node.value);
            this.inorderTraversal(node.right, result);
        }
        return result;
    }

    // Post-order traversal method
    public postorderTraversal(node: TreeNode | undefined, result: number[] = []): number[] {
        if (node) {
            this.postorderTraversal(node.left, result);
            this.postorderTraversal(node.right, result);
            result.push(node.value);
        }
        return result;
    }
}