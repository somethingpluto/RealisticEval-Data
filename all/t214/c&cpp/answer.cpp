#include <iostream>
#include <fstream>
#include <vector>
#include <regex>
#include <string>
#include <stdexcept>

// Define a struct to hold the compiled regex and replacement string
struct Mapping {
    std::regex pattern;
    std::string replacement;
};

std::vector<Mapping> read_mapping_file(const std::string& mapping_file_path) {
    std::vector<Mapping> mappings;

    // Open the file
    std::ifstream mapping_file(mapping_file_path);
    if (!mapping_file.is_open()) {
        throw std::runtime_error("Unable to find the specified file: " + mapping_file_path);
    }

    std::string line;
    while (std::getline(mapping_file, line)) {
        size_t comma_pos = line.find(',');
        if (comma_pos == std::string::npos) {
            throw std::runtime_error("Each line must contain exactly one comma separating the pattern and the replacement.");
        }

        std::string old_pattern = line.substr(0, comma_pos);
        std::string new_word = line.substr(comma_pos + 1);

        // Trim leading and trailing spaces and single quotes
        old_pattern.erase(0, old_pattern.find_first_not_of(" '"));
        old_pattern.erase(old_pattern.find_last_not_of(" '") + 1);
        new_word.erase(0, new_word.find_first_not_of(" '"));
        new_word.erase(new_word.find_last_not_of(" '") + 1);

        // Compile the regex pattern
        mappings.emplace_back(Mapping{std::regex(old_pattern), new_word});
    }

    return mappings;
}
