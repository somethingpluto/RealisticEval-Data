
/**
 * Represents a node in a binary tree.
 */
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
/**
 * Calculates the average value of nodes at each level in a binary tree.
 *
 * @param root The root of the binary tree.
 * @return A list containing the average values of each level.
 */
public static List<Double> averageOfLevels(TreeNode root) {

}