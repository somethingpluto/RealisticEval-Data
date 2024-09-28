#define CATCH_CONFIG_MAIN // This tells Catch to provide a main() - only do this in one cpp file
#include "catch.hpp"
#include <vector>
#include <algorithm>

int minRemovalsToMakeUnique(std::vector<int>& nums) {
    std::vector<int> numbers;
    int minimumDistinct = 0;
    
    for (int number : nums) {
        auto it = std::find(numbers.begin(), numbers.end(), number);
        if (it != numbers.end()) {
            ++minimumDistinct;
            numbers.erase(it);
        }
        numbers.push_back(number);
    }
    
    return minimumDistinct;
}

TEST_CASE("Basic array where multiple removals are needed", "[minRemovalsToMakeUnique]") {
    std::vector<int> nums = {3, 3, 1, 2, 2, 1};
    REQUIRE(minRemovalsToMakeUnique(nums) == 3);
}

TEST_CASE("Array where all elements are identical", "[minRemovalsToMakeUnique]") {
    std::vector<int> nums = {4, 4, 4, 4};
    REQUIRE(minRemovalsToMakeUnique(nums) == 3);
}

TEST_CASE("Array where all elements are already unique", "[minRemovalsToMakeUnique]") {
    std::vector<int> nums = {1, 2, 3, 4};
    REQUIRE(minRemovalsToMakeUnique(nums) == 0);
}

TEST_CASE("Empty array", "[minRemovalsToMakeUnique]") {
    std::vector<int> nums = {};
    REQUIRE(minRemovalsToMakeUnique(nums) == 0);
}

TEST_CASE("Complex case with a larger array", "[minRemovalsToMakeUnique]") {
    std::vector<int> nums = {1, 2, 2, 3, 3, 3, 4, 4, 4, 4};
    REQUIRE(minRemovalsToMakeUnique(nums) == 6);
}