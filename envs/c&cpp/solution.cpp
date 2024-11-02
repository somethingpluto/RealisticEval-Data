#include <iostream>
#include <vector>
#include <unordered_set>

int min_removals_to_make_unique(const std::vector<int>& nums) {
    std::unordered_set<int> seen;
    int minimumDistinct = 0;

    for (int number : nums) {
        // Check if the number has been seen before
        if (seen.count(number) > 0) {
            // If seen, we need to remove one occurrence
            minimumDistinct++;
        } else {
            // If not seen, add it to the set
            seen.insert(number);
        }
    }

    return minimumDistinct;
}
