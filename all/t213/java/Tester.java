package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertArrayEquals;
import org.nd4j.linalg.api.ndarray.INDArray;
import org.nd4j.linalg.factory.Nd4j;

public class Tester {

    private INDArray im2col(INDArray image, int filterHeight, int filterWidth, int stride, int padding) {
        int C = image.size(0);
        int H = image.size(1);
        int W = image.size(2);

        int outHeight = (H + 2 * padding - filterHeight) / stride + 1;
        int outWidth = (W + 2 * padding - filterWidth) / stride + 1;

        // Apply padding to the image
        INDArray paddedImage = Nd4j.create(new int[]{C, H + 2 * padding, W + 2 * padding});
        for (int c = 0; c < C; c++) {
            for (int h = 0; h < H; h++) {
                for (int w = 0; w < W; w++) {
                    paddedImage.putScalar(new int[]{c, h + padding, w + padding}, image.getDouble(c, h, w));
                }
            }
        }

        // Initialize the column matrix
        INDArray col = Nd4j.create(new int[]{C * filterHeight * filterWidth, outHeight * outWidth});

        // Fill the column matrix
        int colIdx = 0;
        for (int y = 0; y <= H + 2 * padding - filterHeight; y += stride) {
            for (int x = 0; x <= W + 2 * padding - filterWidth; x += stride) {
                INDArray patch = paddedImage.get(Nd4j.interval(0, C),
                                                 Nd4j.interval(y, y + filterHeight),
                                                 Nd4j.interval(x, x + filterWidth));
                col.putColumn(colIdx++, patch.ravel());
            }
        }

        return col;
    }

    @Test
    public void testSingleChannelNoPaddingStride1() {
        INDArray image = Nd4j.create(new double[][][] {
            {{1, 2, 3, 4},
             {5, 6, 7, 8},
             {9, 10, 11, 12},
             {13, 14, 15, 16}}
        });  // Shape (1, 4, 4)

        int filterHeight = 2;
        int filterWidth = 2;
        int stride = 1;
        int padding = 0;

        INDArray expectedOutput = Nd4j.create(new double[][] {
            {1, 2, 3, 5, 6, 7, 9, 10, 11},
            {2, 3, 4, 6, 7, 8, 10, 11, 12},
            {5, 6, 7, 9, 10, 11, 13, 14, 15},
            {6, 7, 8, 10, 11, 12, 14, 15, 16}
        });

        INDArray output = im2col(image, filterHeight, filterWidth, stride, padding);
        assertArrayEquals(expectedOutput.data().asDouble(), output.data().asDouble(), 0.0);
    }

    @Test
    public void testSingleChannelNoPaddingStride2() {
        INDArray image = Nd4j.create(new double[][][] {
            {{1, 2, 3, 4},
             {5, 6, 7, 8},
             {9, 10, 11, 12},
             {13, 14, 15, 16}}
        });  // Shape (1, 4, 4)

        int filterHeight = 2;
        int filterWidth = 2;
        int stride = 2;
        int padding = 0;

        INDArray expectedOutput = Nd4j.create(new double[][] {
            {1, 3, 9, 11},
            {2, 4, 10, 12},
            {5, 7, 13, 15},
            {6, 8, 14, 16}
        });

        INDArray output = im2col(image, filterHeight, filterWidth, stride, padding);
        assertArrayEquals(expectedOutput.data().asDouble(), output.data().asDouble(), 0.0);
    }

    @Test
    public void testMultiChannelNoPaddingStride1() {
        INDArray image = Nd4j.create(new double[][][] {
            {{1, 2, 3},
             {4, 5, 6},
             {7, 8, 9}},
            {{9, 8, 7},
             {6, 5, 4},
             {3, 2, 1}}
        });  // Shape (2, 3, 3), 2 channels

        int filterHeight = 2;
        int filterWidth = 2;
        int stride = 1;
        int padding = 0;

        INDArray expectedOutput = Nd4j.create(new double[][] {
            {1, 2, 4, 5},
            {2, 3, 5, 6},
            {4, 5, 7, 8},
            {5, 6, 8, 9},
            {9, 8, 6, 5},
            {8, 7, 5, 4},
            {6, 5, 3, 2},
            {5, 4, 2, 1}
        });

        INDArray output = im2col(image, filterHeight, filterWidth, stride, padding);
        assertArrayEquals(expectedOutput.data().asDouble(), output.data().asDouble(), 0.0);
    }
}