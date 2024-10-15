#include <vector>

std::vector<int> removeElementInArray(const std::vector<int>& array, int element) {
    std::vector<int> newArray;

    for (const auto& item : array) {
        if (item != element) {
            newArray.push_back(item); // Add elements that are not the target element
        }
    }

    return newArray; // Return a new array that does not include the specified element
}