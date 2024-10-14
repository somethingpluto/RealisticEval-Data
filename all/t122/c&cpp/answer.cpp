#include <vector>
#include <optional>

std::vector<int> safeSplice(const std::vector<int>& inputArray, int amountToRemove, int indexToRemove, std::optional<int> replaceWith) {
    std::vector<int> result;

    // Add elements before the indexToRemove
    result.insert(result.end(), inputArray.begin(), inputArray.begin() + indexToRemove);

    // If replaceWith is provided, add it
    if (replaceWith.has_value()) {
        result.push_back(replaceWith.value());
    }

    // Add elements after the removed portion
    result.insert(result.end(), inputArray.begin() + indexToRemove + amountToRemove, inputArray.end());

    return result;
}