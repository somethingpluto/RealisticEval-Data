#include <iostream>
#include <vector>
#include <map>
#include <stdexcept>

// Function to convert a map of vectors into a vector of maps
std::vector<std::map<std::string, int>> dict_of_lists_to_list_of_dicts(const std::map<std::string, std::vector<int>>& dict_of_lists) {
    // Check if all vectors are of the same length
    if (dict_of_lists.empty()) {
        return {};
    }

    size_t expected_length = dict_of_lists.begin()->second.size();
    for (const auto& pair : dict_of_lists) {
        if (pair.second.size() != expected_length) {
            throw std::invalid_argument("All vectors in the dictionary must have the same length.");
        }
    }

    // Using indices to iterate over vectors simultaneously
    std::vector<std::map<std::string, int>> list_of_dicts;
    for (size_t i = 0; i < expected_length; ++i) {
        std::map<std::string, int> current_dict;
        for (const auto& pair : dict_of_lists) {
            current_dict[pair.first] = pair.second[i];
        }
        list_of_dicts.push_back(current_dict);
    }

    return list_of_dicts;
}

int main() {
    try {
        std::map<std::string, std::vector<int>> dict_of_lists = {
            {"a", {1, 2, 3}},
            {"b", {4, 5, 6}}
        };

        auto list_of_dicts = dict_of_lists_to_list_of_dicts(dict_of_lists);

        for (const auto& dict : list_of_dicts) {
            for (const auto& pair : dict) {
                std::cout << pair.first << ": " << pair.second << " ";
            }
            std::cout << std::endl;
        }
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0;
}