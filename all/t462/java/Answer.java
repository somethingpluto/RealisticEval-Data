import java.util.ArrayList;
import java.util.List;

public class Answer {
    public static List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> result = new ArrayList<>();

        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return result;
        }

        int top = 0, bottom = matrix.length - 1;
        int left = 0, right = matrix[0].length - 1;

        while (true) {
            // Traverse from left to right along the top row
            for (int i = left; i <= right; ++i) {
                result.add(matrix[top][i]);
            }
            ++top;
            if (top > bottom) break;

            // Traverse downwards along the right column
            for (int i = top; i <= bottom; ++i) {
                result.add(matrix[i][right]);
            }
            --right;
            if (left > right) break;

            // Traverse from right to left along the bottom row
            for (int i = right; i >= left; --i) {
                result.add(matrix[bottom][i]);
            }
            --bottom;
            if (top > bottom) break;

            // Traverse upwards along the left column
            for (int i = bottom; i >= top; --i) {
                result.add(matrix[i][left]);
            }
            ++left;
            if (left > right) break;
        }

        return result;
    }
}
