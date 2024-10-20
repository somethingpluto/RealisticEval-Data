/**
 * Represents a binary tree node.
 */
public class TreeNode {
    private int value;
    private TreeNode left;
    private TreeNode right;

    /**
     * Constructs a new TreeNode with the specified value and optional children.
     *
     * @param value the value of the node
     * @param left  the left child of the node
     * @param right the right child of the node
     */
    public TreeNode(int value, TreeNode left, TreeNode right) {
        this.value = value;
        this.left = left;
        this.right = right;
    }

    /**
     * Constructs a new TreeNode with the specified value and no children.
     *
     * @param value the value of the node
     */
    public TreeNode(int value) {
        this(value, null, null);
    }

    // Getters and setters for the fields
    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public TreeNode getLeft() {
        return left;
    }

    public void setLeft(TreeNode left) {
        this.left = left;
    }

    public TreeNode getRight() {
        return right;
    }

    public void setRight(TreeNode right) {
        this.right = right;
    }
}

/**
 * Represents a binary tree.
 */
public class BinaryTree {
    private TreeNode root;

    /**
     * Constructs a new BinaryTree with the specified root node.
     *
     * @param root the root node of the tree
     */
    public BinaryTree(TreeNode root) {
        this.root = root;
    }

    /**
     * Constructs a new BinaryTree with no root node.
     */
    public BinaryTree() {
        this(null);
    }

    /**
     * Performs a preorder traversal of the binary tree.
     *
     * @param node   the current node being visited
     * @param result the list to store the traversal results
     * @return the list containing the preorder traversal results
     */
    public List<Integer> preorderTraversal(TreeNode node) {}

    /**
     * Performs an inorder traversal of the binary tree.
     *
     * @param node   the current node being visited
     * @param result the list to store the traversal results
     * @return the list containing the inorder traversal results
     */
    public List<Integer> inorderTraversal(TreeNode node) {}

    /**
     * Performs a postorder traversal of the binary tree.
     *
     * @param node   the current node being visited
     * @param result the list to store the traversal results
     * @return the list containing the postorder traversal results
     */
    public List<Integer> postorderTraversal(TreeNode node) {}
}