#include <iostream>
#include <string>
#include <regex>

/**
 * Extracts a numeric value from the input string based on the given regex pattern.
 *
 * @param x The input from which to extract the value. It will be converted to a string.
 * @param pattern The regular expression pattern to use for matching.
 * @return The extracted weight value if a match is found, otherwise an empty string.
 */
std::string clean_pattern(const std::string& x, const std::string& pattern) {
    // Search for the pattern in the input string
    std::smatch match;
    std::regex regexPattern(pattern);

    if (std::regex_search(x, match, regexPattern)) {
        // Extract the weight value from the first matching group
        std::string weight = match[1].str();  // Can also use match[3] if needed

        try {
            // Convert the weight to a float and return it
            float weightValue = std::stof(weight);
            return std::to_string(weightValue);
        } catch (const std::invalid_argument& e) {
            // Handle cases where conversion to float fails
            std::cerr << "Warning: Unable to convert '" << weight << "' to float." << std::endl;
            return "";
        }
    } else {
        return "";  // Return empty string if no match is found
    }
}
