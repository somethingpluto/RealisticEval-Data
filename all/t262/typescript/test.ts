describe('averageOfLevels', () => {
  it('should calculate the average value of nodes on each level for a simple binary tree', () => {
    const root = new TreeNode(3);
    root.left = new TreeNode(9);
    root.right = new TreeNode(20);
    root.right.left = new TreeNode(15);
    root.right.right = new TreeNode(7);

    const result = averageOfLevels(root);
    expect(result).toEqual([3, 14.5, 11]);
  });

  it('should handle an empty tree', () => {
    const result = averageOfLevels(null);
    expect(result).toEqual([]);
  });
});