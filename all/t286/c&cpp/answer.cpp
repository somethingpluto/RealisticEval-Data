#include <iostream>
#include <optional>

// Function to find the largest integer between n and half of n that is divisible by 5.
std::optional<int> find_largest_divisible(int n) {
    // Start checking from n and go down to half of n
    int start = n;
    int end = n / 2;

    for (int i = start; i > end; --i) {
        if (i % 5 == 0) {
            return i;
        }
    }

    return std::nullopt;  // Return std::nullopt if no number divisible by 5 is found
}
