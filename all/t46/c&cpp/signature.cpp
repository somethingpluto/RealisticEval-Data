// TreeNode class definition
class TreeNode {
public:
    // Binary tree node
    int value;
    TreeNode* left;
    TreeNode* right;

    // Constructor for TreeNode
    TreeNode(int val = 0, TreeNode* l = nullptr, TreeNode* r = nullptr) 
        : value(val), left(l), right(r) {}
};

// BinaryTree class definition
class BinaryTree {
public:
    // Binary tree
    TreeNode* root;

    // Constructor for BinaryTree
    BinaryTree(TreeNode* r = nullptr) : root(r) {}

    // Recursive Preorder Traversal
    std::vector<int> preorder_traversal(TreeNode* node, std::vector<int>* result = nullptr) {}

    // Recursive Inorder Traversal
    std::vector<int> inorder_traversal(TreeNode* node, std::vector<int>* result = nullptr) {}

    // Recursive Postorder Traversal
    std::vector<int> postorder_traversal(TreeNode* node, std::vector<int>* result = nullptr) {}
};