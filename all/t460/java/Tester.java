import org.junit.Test;
import static org.junit.Assert.assertEquals;
import java.util.ArrayList;
import java.util.List;

public class Tester {

    private static final double DELTA = 1e-15;

    @Test
    public void testNonSquareMatrix() {
        List<List<Double>> matrix = new ArrayList<>();
        matrix.add(List.of(1.0, 2.0));
        matrix.add(List.of(3.0, 4.0));
        matrix.add(List.of(5.0, 6.0));

        List<Double> vector = List.of(2.0, 3.0);
        List<Double> expectedResult = List.of(8.0, 18.0, 28.0);

        List<Double> result = matrixVectorMultiplication(matrix, vector);
        assertEquals(expectedResult, result, DELTA);
    }

    @Test
    public void testZeroVector() {
        List<List<Double>> matrix = new ArrayList<>();
        matrix.add(List.of(1.0, 2.0, 3.0));
        matrix.add(List.of(4.0, 5.0, 6.0));

        List<Double> vector = List.of(0.0, 0.0, 0.0);
        List<Double> expectedResult = List.of(0.0, 0.0);

        List<Double> result = matrixVectorMultiplication(matrix, vector);
        assertEquals(expectedResult, result, DELTA);
    }

    @Test
    public void testSingleElement() {
        List<List<Double>> matrix = new ArrayList<>();
        matrix.add(List.of(5.0));

        List<Double> vector = List.of(3.0);
        List<Double> expectedResult = List.of(15.0);

        List<Double> result = matrixVectorMultiplication(matrix, vector);
        assertEquals(expectedResult, result, DELTA);
    }

    @Test
    public void testSingleElementMatrixAndVector() {
        List<List<Double>> matrix = new ArrayList<>();
        matrix.add(List.of(3.0));

        List<Double> vector = List.of(4.0);
        List<Double> expected = List.of(12.0);

        List<Double> result = matrixVectorMultiplication(matrix, vector);
        assertEquals(expected, result, DELTA);
    }

    @Test
    public void testCompatibleSizes() {
        List<List<Double>> matrix = new ArrayList<>();
        matrix.add(List.of(1.0, 2.0, 3.0));
        matrix.add(List.of(4.0, 5.0, 6.0));
        matrix.add(List.of(7.0, 8.0, 9.0));

        List<Double> vector = List.of(1.0, 1.0, 1.0);
        List<Double> expected = List.of(6.0, 15.0, 24.0);

        List<Double> result = matrixVectorMultiplication(matrix, vector);
        assertEquals(expected, result, DELTA);
    }

    // Method for matrix-vector multiplication
    private List<Double> matrixVectorMultiplication(List<List<Double>> matrix, List<Double> vector) {
        // Ensure matrix dimensions are compatible with vector length
        if (matrix.isEmpty() || matrix.get(0).size() != vector.size()) {
            throw new IllegalArgumentException("Matrix and vector dimensions are not compatible for multiplication");
        }

        // Initialize the result list with zeros
        List<Double> result = new ArrayList<>(matrix.size());
        for (int i = 0; i < matrix.size(); i++) {
            result.add(0.0);
        }

        // Perform the matrix-vector multiplication
        for (int i = 0; i < matrix.size(); i++) {
            for (int j = 0; j < vector.size(); j++) {
                result.set(i, result.get(i) + matrix.get(i).get(j) * vector.get(j));
            }
        }

        return result;
    }
}