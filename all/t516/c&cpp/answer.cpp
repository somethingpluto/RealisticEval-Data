#include <iostream>
#include <fstream>
#include <yaml-cpp/yaml.h>
#include <filesystem>

namespace fs = std::filesystem;

// Function to read a YAML file and return its content as a YAML node
YAML::Node read_yaml(const std::string& file_path) {
    // Check if the file exists
    if (!fs::exists(file_path)) {
        throw std::runtime_error("The file '" + file_path + "' does not exist.");
    }

    std::ifstream file(file_path);
    if (!file.is_open()) {
        throw std::runtime_error("Failed to open the file '" + file_path + "'.");
    }

    try {
        // Load the YAML file content
        YAML::Node data = YAML::Load(file);
        return data;
    } catch (const YAML::ParserException& e) {
        throw std::runtime_error("Error parsing YAML file: " + std::string(e.what()));
    }
}