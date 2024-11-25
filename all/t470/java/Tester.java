package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertArrayEquals;
import org.nd4j.linalg.api.ndarray.INDArray;
import org.nd4j.linalg.factory.Nd4j;

public class Tester {


    @Test
    public void testIdentityShear() {
        // Test with zero shear factor which should return the original matrix unchanged.
        INDArray matrix = Nd4j.create(new double[][]{
            {1, 2},
            {3, 4}
        });
        double shearFactor = 0;
        INDArray expectedOutput = Nd4j.create(new double[][]{
            {1, 2},
            {3, 4}
        });
        INDArray result = applyShearX(matrix, shearFactor);
        assertArrayEquals(expectedOutput.data().asDouble(), result.data().asDouble(), 0.0);
    }

    @Test
    public void testPositiveShear() {
        // Test with a positive shear factor.
        INDArray matrix = Nd4j.create(new double[][]{
            {1, 2},
            {3, 4}
        });
        double shearFactor = 1;
        INDArray expectedOutput = Nd4j.create(new double[][]{
            {1, 3},
            {3, 7}
        });
        INDArray result = applyShearX(matrix, shearFactor);
        assertArrayEquals(expectedOutput.data().asDouble(), result.data().asDouble(), 0.0);
    }

    @Test
    public void testNegativeShear() {
        // Test with a negative shear factor.
        INDArray matrix = Nd4j.create(new double[][]{
            {1, 2},
            {3, 4}
        });
        double shearFactor = -1;
        INDArray expectedOutput = Nd4j.create(new double[][]{
            {1, 1},
            {3, 1}
        });
        INDArray result = applyShearX(matrix, shearFactor);
        assertArrayEquals(expectedOutput.data().asDouble(), result.data().asDouble(), 0.0);
    }

    @Test
    public void testHighShearFactor() {
        // Test with a high shear factor to see how the matrix adapts to extreme transformations.
        INDArray matrix = Nd4j.create(new double[][]{
            {1, 1},
            {1, 1}
        });
        double shearFactor = 10;
        INDArray expectedOutput = Nd4j.create(new double[][]{
            {1, 11},
            {1, 11}
        });
        INDArray result = applyShearX(matrix, shearFactor);
        assertArrayEquals(expectedOutput.data().asDouble(), result.data().asDouble(), 0.0);
    }
}