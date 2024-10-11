/**
 * Convert the input string. First, check if it is an integer; if so, convert it to an integer.
 * If it is not an integer, check if it is a floating point number; if yes, convert it to a floating point number.
 * If neither, return the original string.
 *
 * @param value The input value as a string.
 * @return std::variant<int, float, std::string> The converted result.
 */
std::variant<int, float, std::string> numerical_str_convert(const std::string& value);