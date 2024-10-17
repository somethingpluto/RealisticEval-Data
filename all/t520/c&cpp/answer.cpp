#include <cstdint>  // For uint8_t, etc.
#include <cstring>  // For std::memcpy
#include <algorithm>  // For std::reverse

// Function to compute the output index from two given indices in the MultiVector's representation
// of the G_n orthonormal basis.
//
// This function interprets the integers as little-endian bitstrings, takes their XOR,
// and interprets the result as an integer in little-endian.
//
// Args:
//     idx_1 (uint64_t): Input index 1.
//     idx_2 (uint64_t): Input index 2.
//
// Returns:
//     uint64_t: The computed output index.
uint64_t compute_output_index(uint64_t idx_1, uint64_t idx_2) {
    // Perform bitwise XOR between the two indices
    uint64_t result = idx_1 ^ idx_2;

    // Calculate the number of bytes needed to represent the result
    size_t num_bytes = (sizeof(result) * 8 - result.leading_zeros()) / 8;
    if ((sizeof(result) * 8 - result.leading_zeros()) % 8 != 0) {
        num_bytes++;
    }

    // Allocate a buffer to hold the little-endian bytes
    uint8_t* result_bytes = new uint8_t[num_bytes];

    // Copy the result into the buffer in big-endian format
    std::memcpy(result_bytes, &result, num_bytes);

    // Reverse the byte order to make it little-endian
    std::reverse(result_bytes, result_bytes + num_bytes);

    // Convert little-endian bytes back to an integer
    uint64_t result_int = 0;
    for (size_t i = 0; i < num_bytes; ++i) {
        result_int |= static_cast<uint64_t>(result_bytes[i]) << (i * 8);
    }

    // Clean up the allocated buffer
    delete[] result_bytes;

    return result_int;
}