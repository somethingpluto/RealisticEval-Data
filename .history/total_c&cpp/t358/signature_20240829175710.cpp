/**
 * @brief Sort the string array with the shape of "name + number" in ascending order. If the numbers are the same, sort by name in ascending order, and return the sorted array
 *
 * This function sorts a vector of strings where each string is in the format "name + number".
 * Sorting is first done by the numeric part in ascending order, and if two strings have the same
 * numeric part, they are further sorted by the name part in ascending order.
 *
 * @param arr A reference to the vector of strings to be sorted.
 * @return A vector of strings sorted according to the rules described above.
 */
vector<string> sortNames(vector<string> arr) {