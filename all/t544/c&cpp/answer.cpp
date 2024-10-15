#include <vector>

/**
 * Filters out all even numbers from an array.
 *
 * @param array - The vector of numbers to filter.
 * @returns A new vector containing only the odd numbers.
 */
std::vector<int> filterOutEvenNumbers(const std::vector<int>& array) {
    std::vector<int> oddNumbers;
    
    // Iterate through the input array and collect odd numbers
    for (int num : array) {
        if (num % 2 != 0) {
            oddNumbers.push_back(num);
        }
    }
    
    return oddNumbers;
}