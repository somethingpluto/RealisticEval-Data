/**
 * Apply the im2col operation to an input image.
 *
 * @param {Float32Array} image - The input image of shape [C, H, W] where:
 *   C: Number of channels
 *   H: Height of the image
 *   W: Width of the image
 * @param {number} filterHeight - Height of the filter
 * @param {number} filterWidth - Width of the filter
 * @param {number} [stride=1] - Stride of the filter
 * @param {number} [padding=0] - Number of pixels to pad the input image
 * @returns {Float32Array} A 2D array where each column is a flattened filter region
 */
function im2col(image, filterHeight, filterWidth, stride = 1, padding = 0) {}