/**
 * @brief Finds two indices of numbers in the input array that add up to a specified target sum.
 *
 *
 * @param nums The input array of integers.
 *             Must be a vector of integers with at least two elements.
 * @type nums std::vector<int>
 *
 * @param target The target sum value that two numbers from the array should add up to.
 * @type target int
 *
 * @return A vector containing the indices of the two numbers that sum to the target.
 * @rtype std::vector<int>
 *
 * @throws std::invalid_argument If no such indices are found.
 */
std::vector<int> two_sum(const std::vector<int>& nums, int target);