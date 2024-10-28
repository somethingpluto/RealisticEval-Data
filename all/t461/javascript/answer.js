class TreeNode {
    /** 
     * Definition for a binary tree node. 
     * @param {number} val 
     * @param {TreeNode|null} left 
     * @param {TreeNode|null} right 
     */
    constructor(val = 0, left = null, right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

/**
 * Calculate the average value of nodes at each level of a binary tree.
 * 
 * @param {TreeNode|null} root - The root of the binary tree.
 * @returns {number[]} A list of averages for each level of the binary tree.
 */
function averageOfLevels(root) {
    if (!root) {
        return [];
    }

    const averages = []; // List to store the average of each level
    const queue = [root]; // Queue for level-order traversal

    while (queue.length > 0) {
        let levelSum = 0; // Sum of node values at the current level
        const levelCount = queue.length; // Number of nodes at the current level

        // Process all nodes at the current level
        for (let i = 0; i < levelCount; i++) {
            const node = queue.shift(); // Dequeue the front node
            levelSum += node.val; // Add the node's value to the level sum

            // Enqueue child nodes
            if (node.left) {
                queue.push(node.left);
            }
            if (node.right) {
                queue.push(node.right);
            }
        }

        // Calculate the average value for the current level
        const levelAverage = levelSum / levelCount;
        averages.push(levelAverage); // Append average to the result list
    }

    return averages;
}
