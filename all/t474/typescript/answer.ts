function areSiblings(tree: number[], val1: number, val2: number): boolean {
    if (val1 === val2) {
        return false;  // A node cannot be a sibling to itself
    }

    try {
        // Find indices of the values
        const index1 = tree.indexOf(val1);
        const index2 = tree.indexOf(val2);

        if (index1 === -1 || index2 === -1) {
            return false;  // One of the values is not in the tree
        }

        // Check if they have the same parent
        return (index1 - 1) / 2 === Math.floor((index2 - 1) / 2) && index1 !== index2;
    } catch (error) {
        // One of the values is not in the tree
        return false;
    }
}