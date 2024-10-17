#include <iostream>
#include <fstream>
#include <vector>
#include <nlohmann/json.hpp>
#include <filesystem>

namespace fs = std::filesystem;

using json = nlohmann::json;
using json_list = std::vector<json>;

json_list read_jsonl(const std::string& file_path) {
    // Check if the file exists
    if (!fs::exists(file_path)) {
        throw std::runtime_error("The file '" + file_path + "' does not exist.");
    }

    json_list result;
    std::ifstream file(file_path);
    if (!file.is_open()) {
        throw std::runtime_error("Failed to open file: " + file_path);
    }

    try {
        for (std::string line; std::getline(file, line); ) {
            json json_obj = json::parse(line);
            result.push_back(json_obj);
        }
    } catch (const std::exception& e) {
        throw std::runtime_error("Error parsing line: " + line + " - " + e.what());
    }

    return result;
}
