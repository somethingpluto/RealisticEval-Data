import org.junit.Test;
import static org.junit.Assert.assertEquals;
import java.util.List;
import java.util.ArrayList;

public class Tester {

    private List<List<Integer>> transposeMatrix(List<List<Integer>> matrix) {
        // Check if the matrix is empty
        if (matrix == null || matrix.isEmpty() || matrix.get(0).isEmpty()) {
            return new ArrayList<>();
        }

        int numRows = matrix.size();
        int numCols = matrix.get(0).size();

        // Initialize the transposed matrix with the correct dimensions
        List<List<Integer>> transposed = new ArrayList<>();
        for (int col = 0; col < numCols; col++) {
            List<Integer> newRow = new ArrayList<>(numRows);
            for (int row = 0; row < numRows; row++) {
                newRow.add(0);
            }
            transposed.add(newRow);
        }

        // Populate the transposed matrix
        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < numCols; j++) {
                transposed.get(j).set(i, matrix.get(i).get(j));
            }
        }

        return transposed;
    }

    @Test
    public void testSquareMatrix() {
        List<List<Integer>> matrix = new ArrayList<>();
        matrix.add(List.of(1, 2));
        matrix.add(List.of(3, 4));
        List<List<Integer>> expected = new ArrayList<>();
        expected.add(List.of(1, 3));
        expected.add(List.of(2, 4));
        List<List<Integer>> result = transposeMatrix(matrix);
        assertEquals(expected, result);
    }

    @Test
    public void testRectangularMatrix() {
        List<List<Integer>> matrix = new ArrayList<>();
        matrix.add(List.of(1, 2, 3));
        matrix.add(List.of(4, 5, 6));
        List<List<Integer>> expected = new ArrayList<>();
        expected.add(List.of(1, 4));
        expected.add(List.of(2, 5));
        expected.add(List.of(3, 6));
        List<List<Integer>> result = transposeMatrix(matrix);
        assertEquals(expected, result);
    }

    @Test
    public void testMatrixWithEmptyRows() {
        List<List<Integer>> matrix = new ArrayList<>();
        matrix.add(new ArrayList<>());
        matrix.add(new ArrayList<>());
        List<List<Integer>> expected = new ArrayList<>();
        List<List<Integer>> result = transposeMatrix(matrix);
        assertEquals(expected, result);
    }

    @Test
    public void testSingleElementMatrix() {
        List<List<Integer>> matrix = new ArrayList<>();
        matrix.add(List.of(5));
        List<List<Integer>> expected = new ArrayList<>();
        expected.add(List.of(5));
        List<List<Integer>> result = transposeMatrix(matrix);
        assertEquals(expected, result);
    }
}