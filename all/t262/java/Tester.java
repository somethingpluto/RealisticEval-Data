import org.junit.jupiter.api.Test;
import java.util.Arrays;
import java.util.List;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class Tester {

    @Test
    public void testAverageOfLevels() {
        // Create a sample binary tree
        TreeNode root = new TreeNode(3);
        root.left = new TreeNode(9);
        root.right = new TreeNode(20);
        root.right.left = new TreeNode(15);
        root.right.right = new TreeNode(7);

        // Expected result
        List<Double> expected = Arrays.asList(3.0, 14.5, 11.0);

        // Actual result
        List<Double> actual = BinaryTreeUtil.averageOfLevels(root);

        // Assert the results
        assertEquals(expected, actual);
    }
}