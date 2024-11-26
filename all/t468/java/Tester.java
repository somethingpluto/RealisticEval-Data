package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertArrayEquals;
import org.nd4j.linalg.api.ndarray.INDArray;
import org.nd4j.linalg.factory.Nd4j;

/**
 * Test class for the getTranslation function.
 */
public class Tester {

    /**
     * Test for the identity matrix (no translation).
     */
    @Test
    public void testIdentityMatrix() {
        INDArray matrix = Nd4j.create(new double[][]{
            {1, 0, 0},
            {0, 1, 0},
            {0, 0, 1}
        });
        INDArray expectedTranslation = Nd4j.create(new double[]{0.0, 0.0});
        
        assertArrayEquals(expectedTranslation, getTranslation(matrix), 1e-6);
    }

    /**
     * Test for a translation matrix (5 in x, 10 in y).
     */
    @Test
    public void testTranslationMatrix() {
        INDArray matrix = Nd4j.create(new double[][]{
            {1, 0, 5},
            {0, 1, 10},
            {0, 0, 1}
        });
        INDArray expectedTranslation = Nd4j.create(new double[]{5.0, 10.0});
        
        assertArrayEquals(expectedTranslation, getTranslation(matrix), 1e-6);
    }

    /**
     * Test for a translation matrix with negative values.
     */
    @Test
    public void testNegativeTranslation() {
        INDArray matrix = Nd4j.create(new double[][]{
            {1, 0, -3},
            {0, 1, -6},
            {0, 0, 1}
        });
        INDArray expectedTranslation = Nd4j.create(new double[]{-3.0, -6.0});
        
        assertArrayEquals(expectedTranslation, getTranslation(matrix), 1e-6);
    }

    // Utility method to get the translation
    private INDArray getTranslation(INDArray matrix) {
        // Ensure the matrix is a 3x3 array
        if (matrix == null || matrix.rows() != 3 || matrix.columns() != 3) {
            throw new IllegalArgumentException("Input must be a 3x3 affine transformation matrix.");
        }

        // Extract the translation components from the matrix
        INDArray translation = matrix.get(NDArrayIndex.interval(0, 2), NDArrayIndex.point(2));

        // Ensure the return type is double
        return translation.castTo(double.class);
    }
}
