#include <vector>
#include <string>
#include <chrono>

using namespace std;

/**
 * @brief Struct to store sorting statistics.
 *
 * This struct holds information about the sorting algorithm used, the size of the array,
 * the number of comparisons made, and the time taken to run the algorithm.
 */
struct Sort_stats {
    string algorithm_name;  ///< Name of the sorting algorithm
    size_t array_size;      ///< Size of the sorted array
    size_t comparisons;     ///< Number of comparisons made during sorting
    double run_time;        ///< Time taken to run the algorithm in milliseconds
};

/**
 * @brief Implements a generic Hill sorting algorithm and returns a custom struct Sort_stats, including the algorithm name, array size, number of comparisons, and run time
 *
 * This function sorts a vector of generic type T using the Shell sort algorithm.
 * The function also collects statistics, such as the number of comparisons and the time taken to sort the array.
 *
 * @tparam T The type of elements in the vector.
 * @param v A reference to the vector to be sorted.
 * @return A Sort_stats struct containing the sorting statistics.
 */
template <typename T>
Sort_stats shell_sort(vector<T>& v) {
    size_t cmp_cnt = 0;
    auto start = chrono::high_resolution_clock::now();

    int n = v.size();
    for (int gap = n / 2; gap > 0; gap /= 2) {
        for (int i = gap; i < n; i++) {
            T temp = v[i];
            int j;
            for (j = i; j >= gap && v[j - gap] > temp; j -= gap) {
                v[j] = v[j - gap];
                cmp_cnt++;
            }
            v[j] = temp;
            cmp_cnt++; // Count the last comparison
        }
    }

    auto end = chrono::high_resolution_clock::now();
    chrono::duration<double, milli> duration = end - start;

    return Sort_stats{"Shell sort", v.size(), cmp_cnt, duration.count()};
}