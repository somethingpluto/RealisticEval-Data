#include <iostream>
#include <vector>
#include <algorithm>
#include <random>

double findMedian(std::vector<int>& arr) {
    // Sort the array in ascending order
    std::sort(arr.begin(), arr.end());

    size_t n = arr.size();
    size_t midIndex = n / 2;

    // Determine if the array length is even or odd and return the median
    if (n % 2 == 0) {
        // Even number of elements: average the two middle elements
        return (arr[midIndex - 1] + arr[midIndex]) / 2.0;
    } else {
        // Odd number of elements: return the middle element
        return arr[midIndex];
    }
}