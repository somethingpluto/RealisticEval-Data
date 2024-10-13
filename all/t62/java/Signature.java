/**
 * Represents a node in a binary tree.
 */
public class TreeNode {
    TreeNode left;
    TreeNode right;
    int val;

    /**
     * Constructs a new TreeNode with the given key.
     *
     * @param key the value of the node
     */
    public TreeNode(int key) {
        this.left = null;
        this.right = null;
        this.val = key;
    }
}

/**
 * Represents a binary tree and implements its traversal methods.
 */
public class BinaryTree {

    /**
     * The root node of the binary tree.
     */
    private TreeNode root;

    /**
     * Constructs a new BinaryTree with no root node.
     */
    public BinaryTree() {
        this.root = null;
    }

    /**
     * Inserts a new node with the given key into the binary tree.
     *
     * @param key the value of the node to insert
     */
    public void insert(int key) {
        // Implementation of insert method
    }

    /**
     * Helper method to insert a new node with the given key into the binary tree.
     *
     * @param node the current node
     * @param key  the value of the node to insert
     */
    private void _insert(TreeNode node, int key) {
        // Implementation of _insert method
    }

    /**
     * Performs an in-order traversal of the binary tree and returns the traversal result.
     *
     * @return an array representing the in-order traversal result
     */
    public int[] inorderTraversal() {
    }

    /**
     * Helper method to perform an in-order traversal of the binary tree.
     *
     * @param node   the current node
     * @param result the list to store the traversal result
     * @return the updated list containing the traversal result
     */
    private java.util.List<Integer> inorderTraversalRecursive(TreeNode node, java.util.List<Integer> result) {
    }

    /**
     * Performs a pre-order traversal of the binary tree and returns the traversal result.
     *
     * @return an array representing the pre-order traversal result
     */
    public int[] preorderTraversal() {
    }

    /**
     * Helper method to perform a pre-order traversal of the binary tree.
     *
     * @param node   the current node
     * @param result the list to store the traversal result
     * @return the updated list containing the traversal result
     */
    private java.util.List<Integer> preorderTraversalRecursive(TreeNode node, java.util.List<Integer> result) {
    }

    /**
     * Performs a post-order traversal of the binary tree and returns the traversal result.
     *
     * @return an array representing the post-order traversal result
     */
    public int[] postorderTraversal() {
    }

    /**
     * Helper method to perform a post-order traversal of the binary tree.
     *
     * @param node   the current node
     * @param result the list to store the traversal result
     * @return the updated list containing the traversal result
     */
    private java.util.List<Integer> postorderTraversalRecursive(TreeNode node, java.util.List<Integer> result) {
    }
}