// Start of the code context
import { TreeNode } from './TreeNode'; // Assuming TreeNode is defined in a separate file

/**
 * Determines if two values are siblings in a binary tree represented as a TreeNode.
 *
 * @param root - The root TreeNode of the binary tree.
 * @param val1 - The first value to check for sibling relationship.
 * @param val2 - The second value to check for sibling relationship.
 * @returns True if val1 and val2 are siblings, False otherwise.
 */
function areSiblings(root: TreeNode | null, val1: number, val2: number): boolean {
    if (!root) return false;

    let siblings = false;
    const queue: TreeNode[] = [root];

    while (queue.length > 0) {
        const levelSize = queue.length;
        for (let i = 0; i < levelSize; i++) {
            const currentNode = queue.shift()!;
            if (siblings) return true;

            if (currentNode.left && currentNode.right) {
                if ((currentNode.left.val === val1 && currentNode.right.val === val2) ||
                    (currentNode.left.val === val2 && currentNode.right.val === val1)) {
                    siblings = true;
                }
            }

            if (currentNode.left) queue.push(currentNode.left);
            if (currentNode.right) queue.push(currentNode.right);
        }
    }

    return siblings;
}
// End of the code context
describe('TestAreSiblings', () => {
    let tree: number[];

    beforeEach(() => {
        // Setting up a binary tree used for all the test cases
        tree = [1, 2, 3, 4, 5, 6, 7];
    });

    it('should return true for siblings', () => {
        // Test with nodes 4 and 5, which are siblings
        const result = areSiblings(tree, 4, 5);
        expect(result).toBe(true);
    });

    it('should return false for non-siblings', () => {
        // Test with nodes 4 and 6, which are not siblings
        const result = areSiblings(tree, 4, 6);
        expect(result).toBe(false);
    });

    it('should return false for root node and another node', () => {
        // Test with node 1 (root) and any other node, should return False
        const result = areSiblings(tree, 1, 2);
        expect(result).toBe(false);
    });

    it('should return false for non-existent values', () => {
        // Test with non-existent values
        const result = areSiblings(tree, 8, 9);
        expect(result).toBe(false);
    });

    it('should return false for the same node', () => {
        // Test with the same node for both values
        const result = areSiblings(tree, 4, 4);
        expect(result).toBe(false);
    });
});
