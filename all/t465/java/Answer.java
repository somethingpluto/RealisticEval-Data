package org.real.temp;

import org.apache.commons.math3.linear.Array2DRowRealMatrix;
import org.apache.commons.math3.linear.RealVector;

public class Answer {

    /**
     * Multiplies a given matrix by a vector using Apache Commons Math library.
     *
     * @param matrix The 2D array (matrix) of shape (m, n).
     * @param vector The 1D array (vector) of shape (n,) that represents a vector
     *               compatible for multiplication with the given matrix.
     * @return A 1D array (resulting vector) of shape (m,) representing the product of
     *         the matrix and the vector.
     */
    public static RealVector matrixVectorMultiplication(double[][] matrix, double[] vector) {
        // Create an Array2DRowRealMatrix instance from the input matrix.
        Array2DRowRealMatrix mat = new Array2DRowRealMatrix(matrix);

        // Create a RealVector instance from the input vector.
        RealVector vec = new ArrayRealVector(vector);

        // Perform matrix-vector multiplication using the multiply method.
        RealVector result = mat.operate(vec);

        // Return the resulting vector from the multiplication.
        return result;
    }

    public static void main(String[] args) {
        // Example usage
        double[][] matrix = {
            {1, 2, 3},
            {4, 5, 6}
        };

        double[] vector = {7, 8, 9};

        RealVector result = matrixVectorMultiplication(matrix, vector);
        System.out.println(result);
    }
}