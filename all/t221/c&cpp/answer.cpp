#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <regex>
#include <nlohmann/json.hpp>

using json = nlohmann::json;

std::vector<json> extract_parse_dicts(const std::string& file_path) {
    std::ifstream file(file_path);
    if (!file.is_open()) {
        throw std::runtime_error("Could not open file");
    }

    std::string line;
    std::vector<json> dicts;

    while (getline(file, line)) {
        // Regex pattern to match Python-like dictionary syntax
        std::regex dict_pattern(R"(\{.*?\})");

        auto words_begin = std::sregex_iterator(line.begin(), line.end(), dict_pattern);
        auto words_end = std::sregex_iterator();

        for (std::sregex_iterator i = words_begin; i != words_end; ++i) {
            std::smatch match = *i;
            std::string dict_str = match.str();
            try {
                // Parse the string as JSON
                json dict = json::parse(dict_str);
                dicts.push_back(dict);
            } catch (const json::parse_error& e) {
                // Handle parsing error (e.g., invalid dictionary syntax)
                std::cerr << "Error parsing dictionary: " << e.what() << std::endl;
            }
        }
    }

    return dicts;
}