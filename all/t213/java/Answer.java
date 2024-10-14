package org.real.temp;

import org.nd4j.linalg.api.ndarray.INDArray;
import org.nd4j.linalg.factory.Nd4j;

public class Answer {

    /**
     * Apply the im2col operation to an input image.
     *
     * @param image        The input image of shape (C, H, W) where:
     *                     C: Number of channels
     *                     H: Height of the image
     *                     W: Width of the image
     * @param filterHeight Height of the filter
     * @param filterWidth  Width of the filter
     * @param stride       Stride of the filter
     * @param padding      Number of pixels to pad the input image
     * @return A 2D array where each column is a flattened filter region
     */
    public static INDArray im2col(INDArray image, int filterHeight, int filterWidth, int stride, int padding) {
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
                INDArray patch = paddedImage.get(Nd4j.indexInterval(0, C),
                        Nd4j.indexInterval(y, y + filterHeight),
                        Nd4j.indexInterval(x, x + filterWidth));
                col.putColumn(colIdx++, patch.reshape(C * filterHeight * filterWidth));
            }
        }

        return col;
    }

    // Example usage or testing can be added here if needed
}
