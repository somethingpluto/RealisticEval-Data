#include <vector>
#include <iostream>

std::vector<int*> elementsBeforeNull(const std::vector<int*>& array) {
    std::vector<int*> result; // Initialize an empty vector to hold the result

    for (const auto& element : array) {
        if (element == nullptr) {
            break; // Exit the loop if null is encountered
        }
        result.push_back(element); // Add the current element to the result vector
    }

    return result; // Return the result vector
}