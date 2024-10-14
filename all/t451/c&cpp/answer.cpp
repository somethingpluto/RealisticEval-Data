#include <opencv2/opencv.hpp>
#include <vector>
#include <iostream>

std::vector<int> convert_image_to_bits(const std::string& image_path) {
    // Read the image in grayscale mode
    cv::Mat image = cv::imread(image_path, cv::IMREAD_GRAYSCALE);

    if (image.empty()) {
        std::cerr << "Error: Could not read the image." << std::endl;
        return {};
    }

    // Convert the image to binary format
    cv::Mat binaryImage;
    cv::threshold(image, binaryImage, 127, 255, cv::THRESH_BINARY);

    // Flatten the binary image into a vector of bits
    std::vector<int> bits;
    for (int i = 0; i < binaryImage.rows; ++i) {
        for (int j = 0; j < binaryImage.cols; ++j) {
            bits.push_back(binaryImage.at<uchar>(i, j));
        }
    }

    return bits;
}

int main() {
    std::string image_path = "path_to_your_image.jpg";
    std::vector<int> bits = convert_image_to_bits(image_path);

    // Print the bits for demonstration purposes
    for (int bit : bits) {
        std::cout << bit;
    }
    std::cout << std::endl;

    return 0;
}
