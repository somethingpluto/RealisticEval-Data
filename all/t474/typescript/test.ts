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