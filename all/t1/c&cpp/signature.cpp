/**
 * @brief Converts a string to a numerical type (int or float) or returns the original string.
 *
 * @param value The string to be converted. It should represent a numerical value.
 * 
 * @return std::variant<int, float, std::string>
 * - On success, returns an integer if the string represents an integer.
 * - Returns a float if the string represents a floating-point number.
 * - If the string cannot be converted to either type, returns the original string.
 * 
 * @exception std::invalid_argument If the input string is not a valid representation of a number.
 * @exception std::out_of_range If the number represented by the string is out of the range of
 *         the target type (int or float).
 */
 std::variant<int, float, std::string> numerical_str_convert(const std::string& value) {}