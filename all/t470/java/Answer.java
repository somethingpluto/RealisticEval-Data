import org.apache.commons.math3.linear.Array2DRowRealMatrix;
import org.apache.commons.math3.linear.RealMatrix;

public class Answer {

    public static RealMatrix applyShearX(RealMatrix matrix, double shearFactor) {
        int rows = matrix.getRowDimension();
        int cols = matrix.getColumnDimension();

        Array2DRowRealMatrix result = new Array2DRowRealMatrix(rows, cols);

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (j == 0) {
                    result.setEntry(i, j, matrix.getEntry(i, j));
                } else {
                    result.setEntry(i, j, matrix.getEntry(i, j - 1) * shearFactor + matrix.getEntry(i, j));
                }
            }
        }

        return result;
    }
}