/**
 * @brief Calculates the average of the last 'period' integers in the given list of values.
 *
 * @param values A vector of integers from which to calculate the average.
 * @type values std::vector<int>
 *
 * @param period The number of last elements to include in the average calculation. 
 *               Must be greater than zero.
 * @type period int
 *
 * @return The average of the last `period` integers, or `std::nan` if the input vector 
 *         does not contain enough elements or if the period is invalid.
 * @rtype double
 */

double calculate(const std::vector<int>& values, int period);