/**
 * find all the characters that can be represented in Shift-JIS, but not in GBK, and return them as an array
 *
 * @return std::vector<char>: A vector of characters that are unique to Shift-JIS, not encodable in GBK.
 */
std::vector<char> findShiftJisNotGbk();