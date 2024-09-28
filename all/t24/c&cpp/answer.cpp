#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <yaml-cpp/yaml.h>
#include <nlohmann/json.hpp>

void convertYamlToJson(const std::string& yamlFile, const std::string& jsonFile) {
    try {
        // Load the YAML file
        YAML::Node yamlData = YAML::LoadFile(yamlFile);
        
        // Convert the YAML node to a JSON object
        nlohmann::json jsonData = nlohmann::json::parse(yamlData.as<std::string>());
        
        // Write the JSON object to a file
        std::ofstream jsonOutput(jsonFile);
        if (!jsonOutput.is_open()) {
            throw std::runtime_error("Could not open JSON file for writing.");
        }
        jsonOutput << std::setw(4) << jsonData << std::endl;
        jsonOutput.close();
        
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }
}

int main(int argc, char* argv[]) {
    if (argc != 3) {
        std::cerr << "Usage: " << argv[0] << " <yaml_file> <json_file>" << std::endl;
        return 1;
    }

    std::string yamlFile = argv[1];
    std::string jsonFile = argv[2];
    
    convertYamlToJson(yamlFile, jsonFile);

    return 0;
}