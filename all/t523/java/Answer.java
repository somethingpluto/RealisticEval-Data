package org.real.temp;

import org.nd4j.linalg.api.ndarray.INDArray;
import org.nd4j.linalg.factory.Nd4j;

public class Answer {

    /**
     * Translate the point cloud by a given vector.
     *
     * @param pointCloud A N x 3 INDArray representing the 3D point cloud.
     * @param translationVector A 1 x 3 INDArray or double array representing the translation vector.
     * @return A N x 3 INDArray of the translated point cloud.
     */
    public static INDArray translatePointCloud(INDArray pointCloud, double[] translationVector) {
        // Ensure the translationVector is an INDArray for broadcasting
        INDArray vectorNdArray = Nd4j.create(translationVector);

        // Check if translationVector is of correct shape
        if (vectorNdArray.length() != 3) {
            throw new IllegalArgumentException("translationVector must be a 1D array of length 3");
        }

        // Translate the point cloud by adding the translation vector to each point
        INDArray translatedPointCloud = pointCloud.add(vectorNdArray);

        return translatedPointCloud;
    }

    public static void main(String[] args) {
        // Example usage
        double[] translationVector = {1.0, 2.0, 3.0};
        INDArray pointCloud = Nd4j.create(new double[][]{
            {1.0, 2.0, 3.0},
            {4.0, 5.0, 6.0}
        });

        INDArray translatedPointCloud = translatePointCloud(pointCloud, translationVector);
        System.out.println(translatedPointCloud);
    }
}