#include <vector>
#include <iostream>

std::vector<unsigned char> bits_to_bytes(const std::vector<int>& bits) {
    std::vector<unsigned char> bytes;
    size_t num_bits = bits.size();

    // Calculate the number of full bytes we can form
    size_t num_full_bytes = num_bits / 8;

    for (size_t i = 0; i < num_full_bytes; ++i) {
        unsigned char byte = 0;

        // Compose the byte from the bits
        for (int j = 0; j < 8; ++j) {
            byte |= static_cast<unsigned char>(bits[i * 8 + j] << (7 - j));
        }

        bytes.push_back(byte);
    }

    return bytes;
}
