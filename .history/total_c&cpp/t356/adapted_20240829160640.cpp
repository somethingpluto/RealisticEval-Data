#include <vector>

/**
 * @brief Implements the Bubble Sort algorithm.
 *
 * This function sorts an array of integers in ascending order using the Bubble Sort algorithm.
 * The algorithm works by repeatedly stepping through the list, comparing adjacent elements, and
 * swapping them if they are in the wrong order. The process is repeated until the list is sorted.
 *
 * @param arr A reference to a vector of integers to be sorted.
 */
void Sort(std::vector<int>& arr) {
    bool swapped;
    int n = arr.size();
    do {
        swapped = false;
        for (int i = 1; i < n; ++i) {
            if (arr[i - 1] > arr[i]) {
                std::swap(arr[i - 1], arr[i]);
                swapped = true;
            }
        }
        --n; // Reduce the range of comparison, as the last element is now sorted
    } while (swapped);
}