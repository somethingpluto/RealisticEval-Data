#include <iostream>
#include <vector>
#include <cassert>

// Function to rotate the elements of a vector to the left by one position.
std::vector<int> rotate_vector_elements(const std::vector<int>& elements) {
    // Rotate the elements of the vector to the left by one position.
    // The first element is moved to the end of the vector,
    // and all other elements are shifted one position to the left.

    if (elements.size() <= 1) {
        return elements;
    }

    std::vector<int> rotated(elements.size());
    std::copy(elements.begin() + 1, elements.end(), rotated.begin());
    rotated.back() = elements.front();

    return rotated;
}

// Function to rotate the elements of a vector, moving the first element to the end and shifting all others forward.
std::vector<int> rotate_vector(const std::vector<int>& elements) {
    // Rotate the elements of the vector, moving the first element to the end and shifting all others forward.

    if (elements.empty()) {
        return elements;  // Return the vector as is if it's empty
    }

    std::vector<int> rotated(elements.size());
    std::copy(elements.begin() + 1, elements.end(), rotated.begin());
    rotated.back() = elements.front();

    return rotated;
}

// Function to check the correctness of the rotate_vector function.
void check_rotate_vector() {
    assert(rotate_vector({}) == std::vector<int>({}));
    assert(rotate_vector({1}) == std::vector<int>({1}));
    assert(rotate_vector({1, 2, 3, 4}) == std::vector<int>({2, 3, 4, 1}));
    assert(rotate_vector({5, 6, 7}) == std::vector<int>({6, 7, 5}));

    std::cout << "All test cases passed!" << std::endl;
}