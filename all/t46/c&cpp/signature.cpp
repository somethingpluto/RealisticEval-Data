class BinaryTree {
private:
    TreeNode* root;

public:
    // Constructor
    BinaryTree(TreeNode* root = nullptr);

    // Preorder traversal
    void preorderTraversal(TreeNode* node, std::vector<int>& result) const;

    // Inorder traversal
    void inorderTraversal(TreeNode* node, std::vector<int>& result) const;

    // Postorder traversal
    void postorderTraversal(TreeNode* node, std::vector<int>& result) const;

    // Helper functions to start traversals from the root
    std::vector<int> getPreorderTraversal() const;
    std::vector<int> getInorderTraversal() const;
    std::vector<int> getPostorderTraversal() const;
};
