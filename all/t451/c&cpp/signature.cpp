/**
 * Converts an image to a binary representation. Convert the image to black and white mode,
 * that is, each pixel is represented by only 1 bit, with a white pixel value of 255 and a black pixel value of 0.
 *
 * @param image_path The file path of the image to convert.
 * @return A vector of integers representing the image, where 1 is for white pixels and 0 is for black pixels.
 */
std::vector<int> convertImageToBits(const std::string& image_path);
