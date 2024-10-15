#include <vector>
#include <functional>

template <typename T>
std::vector<T> filterArray(const std::vector<T>& unfilteredArray, std::function<bool(const T&)> isQualified) {
    std::vector<T> filteredResults;

    // Use a for loop to iterate through each element in the unfiltered array
    for (const auto& element : unfilteredArray) {
        // Check if the current element qualifies
        if (isQualified(element)) {
            // If it qualifies, push it to the results array
            filteredResults.push_back(element);
        }
    }

    return filteredResults; // Return the filtered results
}