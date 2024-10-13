#include <fstream>
#include <iostream>
#include <yaml-cpp/yaml.h>
#include <nlohmann/json.hpp>

using json = nlohmann::json;

void convertYamlToJson(const std::string& yamlFile, const std::string& jsonFile) {
    /**
     * Convert a YAML file to a JSON file.
     *
     * @param yamlFile: Path to the input YAML file.
     * @param jsonFile: Path to the output JSON file.
     */
    try {
        // Read the YAML file
        YAML::Node yamlData = YAML::LoadFile(yamlFile);

        // Convert YAML data to JSON
        json jsonData = json::parse(yamlData.dump());

        // Write the JSON data to a file
        std::ofstream outputFile(jsonFile);
        if (!outputFile.is_open()) {
            throw std::runtime_error("Failed to open JSON file.");
        }
        outputFile << std::setw(4) << jsonData << std::endl;
        outputFile.close();
    } catch (const YAML::Exception& e) {
        std::cerr << "Error loading YAML file: " << e.what() << std::endl;
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }
}

int main() {
    // Example usage
    std::string yamlFilePath = "input.yaml";
    std::string jsonFilePath = "output.json";
    convertYamlToJson(yamlFilePath, jsonFilePath);
    return 0;
}