package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import org.nd4j.linalg.api.ndarray.INDArray;
import org.nd4j.linalg.factory.Nd4j;

public class Tester {

    private static final double DELTA = 1e-15;

    @Test
    public void testSimpleTranslation() {
        // Test a simple translation of a single point
        INDArray pointCloud = Nd4j.create(new double[][]{{1.0, 2.0, 3.0}});
        double[] translationVector = {1.0, 1.0, 1.0};
        INDArray expectedOutput = Nd4j.create(new double[][]{{2.0, 3.0, 4.0}});

        INDArray translatedPointCloud = Answer.translatePointCloud(pointCloud, translationVector);

        assertEquals(String.valueOf(expectedOutput), translatedPointCloud, DELTA);
    }

    @Test
    public void testMultiplePointsTranslation() {
        // Test translation of multiple points
        INDArray pointCloud = Nd4j.create(new double[][]{{1.0, 2.0, 3.0}, {4.0, 5.0, 6.0}});
        double[] translationVector = {1.0, 2.0, 3.0};
        INDArray expectedOutput = Nd4j.create(new double[][]{{2.0, 4.0, 6.0}, {5.0, 7.0, 9.0}});

        INDArray translatedPointCloud = Answer.translatePointCloud(pointCloud, translationVector);

        assertEquals(String.valueOf(expectedOutput), translatedPointCloud, DELTA);
    }

    @Test
    public void testZeroTranslation() {
        // Test translation by a zero vector (should return the same point cloud)
        INDArray pointCloud = Nd4j.create(new double[][]{{1.0, 2.0, 3.0}, {4.0, 5.0, 6.0}});
        double[] translationVector = {0.0, 0.0, 0.0};
        INDArray expectedOutput = pointCloud;  // No change expected

        INDArray translatedPointCloud = Answer.translatePointCloud(pointCloud, translationVector);

        assertEquals(String.valueOf(expectedOutput), translatedPointCloud, DELTA);
    }

    @Test
    public void testNegativeTranslation() {
        // Test translation with negative values
        INDArray pointCloud = Nd4j.create(new double[][]{{1.0, 2.0, 3.0}});
        double[] translationVector = {-1.0, -2.0, -3.0};
        INDArray expectedOutput = Nd4j.create(new double[][]{{0.0, 0.0, 0.0}});

        INDArray translatedPointCloud = Answer.translatePointCloud(pointCloud, translationVector);

        assertEquals(String.valueOf(expectedOutput), translatedPointCloud, DELTA);
    }
}