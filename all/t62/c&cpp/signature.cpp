// TreeNode class represents a node in the binary tree.
class TreeNode {
public:
    // Constructor initializes a new TreeNode with the given key.
    TreeNode(int key) : val(key), left(nullptr), right(nullptr) {}

    // Pointers to the left and right child nodes.
    TreeNode* left;
    TreeNode* right;

    // Value stored in the node.
    int val;
};

// BinaryTree class implements a binary tree with insertion and traversal methods.
class BinaryTree {
public:
    // Constructor initializes the root of the binary tree to null.
    BinaryTree() : root(nullptr) {}

    // Inserts a new node with the given key into the binary tree.
    void insert(int key);

private:
    // Helper function to insert a new node with the given key.
    void _insert(TreeNode* node, int key);

public:
    // Performs an inorder traversal of the binary tree and returns the result.
    std::vector<int> inorder_traversal();

private:
    // Helper function to perform an inorder traversal.
    void _inorder_traversal(TreeNode* node, std::vector<int>& result);

public:
    // Performs a preorder traversal of the binary tree and returns the result.
    std::vector<int> preorder_traversal();

private:
    // Helper function to perform a preorder traversal.
    void _preorder_traversal(TreeNode* node, std::vector<int>& result);

public:
    // Performs a postorder traversal of the binary tree and returns the result.
    std::vector<int> postorder_traversal();

private:
    // Helper function to perform a postorder traversal.
    void _postorder_traversal(TreeNode* node, std::vector<int>& result);

    // Pointer to the root of the binary tree.
    TreeNode* root;
};