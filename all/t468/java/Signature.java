import org.apache.commons.math3.linear.Array2DRowRealMatrix;
import org.apache.commons.math3.linear.RealMatrix;

/**
 * Given a 3x3 matrix, return the corresponding translation vector.
 *
 * @param matrix The 3x3 affine transformation matrix.
 * @return A 2-element array containing the translation components (translation_x, translation_y).
 */
public double[] getTranslation(RealMatrix matrix) {
    // Ensure the input matrix is a 3x3 matrix
    if (matrix.getRowDimension() != 3 || matrix.getColumnDimension() != 3) {
        throw new IllegalArgumentException("Input matrix must be a 3x3 matrix.");
    }

    // Extract the translation vector from the last column of the matrix
    double translationX = matrix.getEntry(0, 2);
    double translationY = matrix.getEntry(1, 2);

    // Return the translation vector as a 2-element array
    return new double[]{translationX, translationY};
}
