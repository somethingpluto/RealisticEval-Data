import static org.junit.Assert.assertArrayEquals;
import org.junit.Test;

public class Tester {

    @Test
    public void testGetTranslation() {
        // Define a sample input matrix
        double[][] matrix = {
            {1.0, 0.0, 5.0},
            {0.0, 1.0, 3.0},
            {0.0, 0.0, 1.0}
        };

        // Call the getTranslation method from MatrixUtils
        double[] result = MatrixUtils.getTranslation(matrix);

        // Expected translation vector
        double[] expected = {5.0, 3.0};

        // Assert that the result matches the expected output
        assertArrayEquals(expected, result, 0.001);
    }
}

// Assuming there's a utility class with the getTranslation method
class MatrixUtils {
    public static double[] getTranslation(double[][] matrix) {
        if (matrix.length != 3 || matrix[0].length != 3 || matrix[1].length != 3 || matrix[2].length != 3) {
            throw new IllegalArgumentException("Input matrix must be 3x3");
        }

        return new double[]{matrix[0][2], matrix[1][2]};
    }
}