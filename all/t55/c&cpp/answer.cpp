#include <iostream>
#include <vector>
#include <unordered_set>
#include <unordered_map>

int minRemovalsToMakeUnique(std::vector<int>& nums) {
    std::unordered_set<int> numbers;
    int minimumDistinct = 0;

    for (int number : nums) {
        if (numbers.find(number) != numbers.end()) {
            minimumDistinct += 1;
        } else {
            numbers.insert(number);
        }
    }

    return minimumDistinct;
}

int main() {
    std::vector<int> nums = {1, 2, 3, 2, 4, 3, 5};
    std::cout << "Minimum removals to make unique: " << minRemovalsToMakeUnique(nums) << std::endl;
    return 0;
}