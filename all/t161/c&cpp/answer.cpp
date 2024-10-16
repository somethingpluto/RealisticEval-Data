#include <iostream>
#include <vector>
#include <map>
#include <string>

void generateCombinationsHelper(const std::vector<std::vector<int>>& values,
                                 std::vector<int>& currentCombination,
                                 int currentIndex,
                                 std::vector<std::vector<int>>& combinations) {
    if (currentIndex == values.size()) {
        combinations.push_back(currentCombination);
        return;
    }

    for (int value : values[currentIndex]) {
        currentCombination[currentIndex] = value;
        generateCombinationsHelper(values, currentCombination, currentIndex + 1, combinations);
    }
}

std::vector<std::vector<int>> generateCombinations(const std::map<std::string, std::vector<int>>& inputMap) {
    std::vector<std::vector<int>> combinations;
    std::vector<std::vector<int>> values;

    for (const auto& pair : inputMap) {
        values.push_back(pair.second);
    }

    std::vector<int> currentCombination(values.size());
    generateCombinationsHelper(values, currentCombination, 0, combinations);

    return combinations;
}