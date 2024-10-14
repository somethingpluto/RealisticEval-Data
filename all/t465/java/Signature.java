import org.apache.commons.math3.linear.Array2DRowRealMatrix;
import org.apache.commons.math3.linear.RealVector;

public class MatrixVectorMultiplication {

    /**
     * Multiplies a given matrix by a vector using Apache Commons Math's RealMatrix and RealVector classes.

     * @param matrix The 2D array (matrix) of shape (m, n) where m is the number of rows
                    and n is the number of columns.
     * @param vector The 1D array (vector) of shape (n,) that represents a vector
                    compatible for multiplication with the given matrix.
     * @return A 1D array (resulting vector) of shape (m,) representing the product of
                the matrix and the vector.
     */
    public static RealVector matrixVectorMultiplication(double[][] matrix, double[] vector) {
        // Create a new Array2DRowRealMatrix object from the provided matrix.
        Array2DRowRealMatrix matrixObj = new Array2DRowRealMatrix(matrix);

        // Create a new RealVector object from the provided vector.
        RealVector vectorObj = new ArrayRealVector(vector);

        // Multiply the matrix by the vector using the multiply method.
        RealVector result = matrixObj.operate(vectorObj);

        // Return the resulting vector from the multiplication.
        return result;
    }
}
