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