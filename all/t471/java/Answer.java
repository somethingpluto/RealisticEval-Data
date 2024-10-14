import org.apache.commons.math3.linear.Array2DRowRealMatrix;
import org.apache.commons.math3.linear.RealMatrix;

public class Answer {
    public static double getRotation(RealMatrix matrix) {
        // Assuming that the input matrix is a 3x3 affine transformation matrix
        if (matrix.getRowDimension() != 3 || matrix.getColumnDimension() != 3) {
            throw new IllegalArgumentException("Input matrix must be a 3x3 matrix");
        }

        // Extracting elements of the matrix
        double m00 = matrix.getEntry(0, 0);
        double m01 = matrix.getEntry(0, 1);
        double m10 = matrix.getEntry(1, 0);
        double m11 = matrix.getEntry(1, 1);

        // Calculating the rotation angle in radians
        double rotationAngle = Math.atan2(m10, m00);

        return rotationAngle;
    }
}
