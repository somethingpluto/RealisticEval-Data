/**
 * Convert the input string, first see if it is an integer, if it is converted to an integer,
 * if it is not, see if it is a floating point number, if yes, convert to a floating point number,
 * if neither, return the original string.
 *
 * @param value The input value string
 * @return std::variant<int, double, std::string> The converted value or the original string
 */
std::variant<int, double, std::string> numericalStrConvert(const std::string& value);