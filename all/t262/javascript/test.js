describe('averageOfLevels', () => {
  it('should return the average values of each level in a binary tree', () => {
    // Constructing the following binary tree:
    //       3
    //      / \
    //     9   20
    //        /  \
    //       15   7
    const root = new TreeNode(3);
    root.left = new TreeNode(9);
    root.right = new TreeNode(20);
    root.right.left = new TreeNode(15);
    root.right.right = new TreeNode(7);

    expect(averageOfLevels(root)).toEqual([3, 14.5, 11]);
  });

  it('should handle an empty tree', () => {
    expect(averageOfLevels(null)).toEqual([]);
  });

  it('should handle a single node tree', () => {
    const root = new TreeNode(5);
    expect(averageOfLevels(root)).toEqual([5]);
  });
});