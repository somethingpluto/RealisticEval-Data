class TreeNode {
    int value;
    TreeNode left;
    TreeNode right;

    /**
     * Constructor for TreeNode
     *
     * @param value The value of the node
     * @param left  The left child node
     * @param right The right child node
     */
    public TreeNode(int value, TreeNode left, TreeNode right) {
        this.value = value;
        this.left = left;
        this.right = right;
    }

    // Default constructor
    public TreeNode() {
        this(0, null, null);
    }
}

/**
 * Binary Tree
 */
class BinaryTree {
    TreeNode root;

    /**
     * Constructor for BinaryTree
     *
     * @param root The root node of the binary tree
     */
    public BinaryTree(TreeNode root) {
       
    }

    /**
     * Pre-order traversal of the binary tree
     *
     * @param node The current node being visited
     * @param result The list to store the traversal result
     */
    public void preorderTraversal(TreeNode node, List<Integer> result) {
        
    }

    /**
     * In-order traversal of the binary tree
     *
     * @param node The current node being visited
     * @param result The list to store the traversal result
     */
    public void inorderTraversal(TreeNode node, List<Integer> result) {
        
    }

    /**
     * Post-order traversal of the binary tree
     *
     * @param node The current node being visited
     * @param result The list to store the traversal result
     */
    public void postorderTraversal(TreeNode node, List<Integer> result) {
        
    }
}