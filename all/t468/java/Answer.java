package org.real.temp;

import java.lang.IllegalArgumentException;
import org.nd4j.linalg.api.ndarray.INDArray;
import org.nd4j.linalg.factory.Nd4j;

public class Answer {

    /**
     * Given a 3x3 matrix, returns the corresponding translation vector.
     * 
     * @param matrix A 3x3 affine transformation matrix.
     * @return A 2-element array containing the translation components (translation_x, translation_y).
     */
    public static INDArray getTranslation(INDArray matrix) {
        // Ensure the matrix is a 3x3 array
        if (matrix == null || matrix.rows() != 3 || matrix.columns() != 3) {
            throw new IllegalArgumentException("Input must be a 3x3 affine transformation matrix.");
        }

        // Extract the translation components from the matrix
        INDArray translation = matrix.get(NDArrayIndex.interval(0, 2), NDArrayIndex.point(2));

        // Ensure the return type is double
        return translation.castTo(double.class);
    }

    public static void main(String[] args) {
        // Example usage
        INDArray matrix = Nd4j.create(new double[][]{
            {1, 0, 10},
            {0, 1, 20},
            {0, 0, 1}
        });

        INDArray translation = getTranslation(matrix);
        System.out.println(translation);
    }
}