#include <regex>
#include <string>

// Extracts the date in the format YYYY-MM-DD from the given file name.
// Args:
//     file_name: The name of the file which may contain a date.
// Returns:
//     A std::string containing the extracted date in YYYY-MM-DD format if found, else an empty string.
std::string extract_date_from_filename(const std::string& file_name) {
    // Define the regex pattern for matching a date in the format YYYY-MM-DD
    std::regex date_pattern(R"(\d{4}-\d{2}-\d{2})");

    // Search for the date pattern in the file name
    std::smatch match;

    // If a match is found, return the matched date; otherwise, return an empty string
    if (std::regex_search(file_name, match, date_pattern)) {
        return match.str(0);
    } else {
        return "";
    }
}