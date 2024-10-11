import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class Tester {
    
    @Test(expected = IllegalArgumentException.class)
    public void testNegativeExponent() {
        int[][] matrix = {{1, 2}, {3, 4}};
        MatrixPower.power(matrix, -1);
    }

    @Test(expected = IllegalArgumentException.class)
    public void testNonIntegerExponent() {
        int[][] matrix = {{1, 2}, {3, 4}};
        MatrixPower.power(matrix, 1.5);
    }

    @Test(expected = IllegalArgumentException.class)
    public void testNonMatrixInput() {
        Object[] input = {"not", "a", "matrix"};
        MatrixPower.power(input, 2);
    }
    
    // Add more tests for other scenarios...
}