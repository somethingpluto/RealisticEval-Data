#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <filesystem>
#include <nlohmann/json.hpp>

using json = nlohmann::json;
namespace fs = std::filesystem;

std::vector<std::string> find_json_files_with_keyword(const std::string& directory, const std::string& keyword) {
    std::vector<std::string> matching_files;

    try {
        for (const auto& entry : fs::recursive_directory_iterator(directory)) {
            if (entry.path().extension() == ".json") {
                std::ifstream file(entry.path());
                if (file.is_open()) {
                    json data;
                    file >> data;

                    std::string data_str = data.dump();
                    if (data_str.find(keyword) != std::string::npos) {
                        matching_files.push_back(entry.path().string());
                    }
                } else {
                    std::cerr << "Error opening file: " << entry.path() << std::endl;
                }
            }
        }
    } catch (const std::exception& e) {
        std::cerr << "Error reading directory " << directory << ": " << e.what() << std::endl;
    }

    return matching_files;
}

int main() {
    std::string directory = "path_to_directory";
    std::string keyword = "search_keyword";

    std::vector<std::string> result = find_json_files_with_keyword(directory, keyword);

    for (const auto& filename : result) {
        std::cout << "Found keyword in: " << filename << std::endl;
    }

    return 0;
}