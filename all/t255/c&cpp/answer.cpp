#include <iostream>
#include <vector>
#include <fstream>

std::vector<int> convertImageToBits(const std::string &imagePath) {
    // Open the file
    std::ifstream file(imagePath);
    if (!file.is_open()) {
        throw std::runtime_error("Could not open image file");
    }

    std::vector<int> bits;

    // Read the file
    char c;
    while (file.get(c)) {
        // Convert character to bit
        int bit = static_cast<int>(c - '0');
        bits.push_back(bit);
    }

    file.close();
    return bits;
}