#include <iostream>
#include <vector>

// Function to convert a list of hole positions to the ring format (vector of 1s and 0s).
std::vector<int> convert_to_ring_format(const std::vector<int>& holes) {
    // Initialize the ring with all positions set to 1
    std::vector<int> ring(32, 1);

    // Mark the positions of holes as 0
    for (int hole : holes) {
        if (0 <= hole && hole < 32) {  // Ensure hole positions are within valid range
            ring[hole] = 0;
        }
    }

    return ring;
}

// Function to check the correctness of the convert_to_ring_format function
void check_function() {
    std::vector<int> holes = {5, 7, 12, 28};
    std::vector<int> expected = {1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1};
    std::vector<int> result = convert_to_ring_format(holes);

    bool correct = true;
    for (size_t i = 0; i < expected.size(); ++i) {
        if (expected[i] != result[i]) {
            correct = false;
            break;
        }
    }

    if (correct) {
        std::cout << "The function works correctly." << std::endl;
    } else {
        std::cout << "The function does not work correctly." << std::endl;
    }
}