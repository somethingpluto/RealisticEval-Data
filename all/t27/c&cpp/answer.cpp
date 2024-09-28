#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <filesystem>
#include <json/json.h>  // Include the jsoncpp header file

namespace fs = std::filesystem;

std::vector<Json::Value> concatenateJsonArrays(const std::string &directory) {
    std::vector<Json::Value> combinedData;

    // Loop through all files in the directory
    for (const auto &entry : fs::directory_iterator(directory)) {
        const std::string filename = entry.path().filename().string();

        // Check if the file is a JSON file
        if (entry.path().extension() == ".json") {
            // Open and read the JSON file
            std::ifstream file(entry.path());
            if (!file.is_open()) {
                std::cerr << "Warning: Could not open " << filename << std::endl;
                continue;
            }
            
            Json::Value data;
            file >> data; // Parse the JSON data

            // Check if the data is a list (array at root)
            if (data.isArray()) {
                for (const auto &item : data) {
                    combinedData.push_back(item);
                }
            } else {
                std::cout << "Warning: " << filename << " does not contain a root-level array." << std::endl;
            }
        }
    }

    return combinedData;
}

int main() {
    std::string directory = "your_directory_here"; // Modify this with your directory path
    std::vector<Json::Value> result = concatenateJsonArrays(directory);

    // Output the combined data (for demonstration purposes)
    for (const auto &item : result) {
        std::cout << item << std::endl;
    }

    return 0;
}