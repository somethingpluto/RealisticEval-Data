#include <vector>

/**
 * Determines if two values are siblings in a binary tree represented as an array.
 *
 * @param tree std::vector<int>, the binary tree level-order representation
 * @param val1 int, first value to check for sibling relationship
 * @param val2 int, second value to check for sibling relationship
 * @return bool, true if val1 and val2 are siblings, false otherwise
 */
bool areSiblings(const std::vector<int>& tree, int val1, int val2);
