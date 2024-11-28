/**
 * Decompose a flat index `n` into a multidimensional index based on the given shape.
 *
 * @param n Flat index (non-negative integer).
 * @param shape Tuple representing the dimensions of the multi-dimensional array.
 * @return Tuple representing the multidimensional index corresponding to `n`.
 * @throws std::out_of_range If `n` is out of bounds for the array defined by `shape`.
 */
std::tuple<int, int, int> decompose(int n, const std::vector<int>& shape) {}