#include <string>
#include <variant>
#include <stdexcept>
#include <sstream>

/**
 * @brief Convert a string representation of a number to an integer, float, or return the original string.
 *
 * This function attempts to parse the input string as an integer first. If the parsing fails, it then tries
 * to parse it as a floating-point number. If both conversions fail, the original string is returned.
 *
 * @param value The input string to be converted.
 * @return std::variant<int, double, std::string> The converted integer or float, or the original string.
 */
std::variant<int, double, std::string> numericalStrConvert(const std::string& value) {}