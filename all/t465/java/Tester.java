import static org.junit.Assert.assertArrayEquals;
import org.junit.Test;

public class Tester {

    @Test
    public void testMatrixVectorMultiplication() {
        double[][] matrix = {{1, 2}, {3, 4}};
        double[] vector = {5, 6};

        // Call the method under test
        double[] result = matrixVectorMultiplication(matrix, vector);

        // Define expected output
        double[] expectedOutput = {17, 39};

        // Assert if the actual output matches the expected output
        assertArrayEquals(expectedOutput, result, 0.0001);
    }

    private double[] matrixVectorMultiplication(double[][] matrix, double[] vector) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        double[] result = new double[rows];

        for(int i=0; i<rows; i++) {
            for(int j=0; j<cols; j++) {
                result[i] += matrix[i][j] * vector[j];
            }
        }

        return result;
    }
}