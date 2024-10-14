public static INDArray im2col(INDArray image, int filterHeight, int filterWidth, int stride, int padding) {
    /**
     * Applies the im2col operation to an input image.
     *
     * @param image        The input image of shape (C, H, W) where:
     *                     C: Number of channels
     *                     H: Height of the image
     *                     W: Width of the image
     * @param filterHeight Height of the filter
     * @param filterWidth  Width of the filter
     * @param stride       Stride of the filter (default is 1)
     * @param padding      Number of pixels to pad the input image (default is 0)
     * @return A 2D array where each column is a flattened filter region
     */
}