describe('averageOfLevels', () => {
    it('should handle an empty tree', () => {
        const root = null;
        const expected = [];
        expect(averageOfLevels(root)).toEqual(expected);
    });

    it('should handle a single-node tree', () => {
        const root = new TreeNode(5);
        const expected = [5.0];
        expect(averageOfLevels(root)).toEqual(expected);
    });

    it('should handle a balanced tree with two levels', () => {
        const root = new TreeNode(3);
        root.left = new TreeNode(9);
        root.right = new TreeNode(20);
        const expected = [3.0, 14.5];  // Level 0: 3; Level 1: (9+20)/2 = 14.5
        expect(averageOfLevels(root)).toEqual(expected);
    });

    it('should handle an unbalanced tree', () => {
        const root = new TreeNode(1);
        root.right = new TreeNode(2);
        root.right.right = new TreeNode(3);
        const expected = [1.0, 2.0, 3.0];  // Level 0: 1; Level 1: 2; Level 2: 3
        expect(averageOfLevels(root)).toEqual(expected);
    });

    it('should handle a tree with multiple levels', () => {
        const root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);
        root.right.right = new TreeNode(8);
        const expected = [1.0, 2.5, 5.67];  // Level 0: 1; Level 1: (2+3)/2 = 2.5; Level 2: (4+5+8)/3 ≈ 5.67
        expect(averageOfLevels(root)[2]).toBeCloseTo(expected[2], 2);
        expect(averageOfLevels(root).slice(0, 2)).toEqual(expected.slice(0, 2));
    });
});