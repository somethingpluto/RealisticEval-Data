/**
 * Decompose a flat index `n` into a multidimensional index based on the given shape.
 *
 * @param n Flat index (non-negative integer).
 * @param shape Tuple representing the dimensions of the multi-dimensional array.
 * @return std::tuple Decomposed multidimensional index corresponding to `n`.
 * @throw std::out_of_range If `n` is out of bounds for the array defined by `shape`.
 */
std::tuple<int, int> decompose(int n, const std::tuple<int, int>& shape){

}