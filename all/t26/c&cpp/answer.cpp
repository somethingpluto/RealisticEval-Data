#include <iostream>
#include <regex>
#include <string>

std::string convert_to_comma_separated(const std::string& input_string) {
    /**
     * Converts an input string with multiple separators to a comma-separated string.
     * Now handles additional separators: hyphens (-) and colons (:).
     *
     * Args:
     * input_string (std::string): The input string containing various separators like *, ;, /, -, :
     *
     * Returns:
     * std::string: A comma-separated string where all specified separators have been replaced with commas.
     */
    // The pattern includes *, ;, /, -, :
    std::regex pattern("[\\*;/-:]");
    std::string comma_separated_string = std::regex_replace(input_string, pattern, ",");
    return comma_separated_string;
}