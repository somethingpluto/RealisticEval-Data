function areSiblings(tree, val1, val2) {
    /**
     * Determines if two values are siblings in a binary tree represented as an array.
     *
     * @param {Array<number>} tree - the binary tree level-order representation
     * @param {number} val1 - first value to check for sibling relationship
     * @param {number} val2 - second value to check for sibling relationship
     * @returns {boolean}
     */

    // Iterate through each element in the tree
    for(let i = 0; i < tree.length; i++) {
        // Check if current node has children
        if (tree[i] !== null && tree[i] !== undefined && tree[i] !== 0) {
            let leftChild = 2 * i + 1;
            let rightChild = 2 * i + 2;

            // Check if either of the child nodes match val1 or val2
            if ((leftChild < tree.length && tree[leftChild] === val1 && tree[rightChild] === val2)
                || (rightChild < tree.length && tree[rightChild] === val1 && tree[leftChild] === val2)) {
                    return true;
                }
        }
    }

    // If no siblings found, return false
    return false;
}
