#include <iostream>
#include <string>
#include <map>
#include <pugixml.hpp>

std::map<std::string, std::string> parse_xaml_to_dict(const std::string& xaml_file) {
    /**
     * Parse a XAML file and extract key-value pairs from 'String' elements.
     *
     * Args:
     * xaml_file (std::string): Path to the XAML file.
     *
     * Returns:
     * std::map<std::string, std::string>: A map containing the key-value pairs extracted from 'String' elements.
     */
    try {
        pugi::xml_document doc;
        if (!doc.load_file(xaml_file.c_str())) {
            std::cerr << "Error: The file " << xaml_file << " does not exist." << std::endl;
            return {};
        }

        // Dictionary to hold the key-value pairs
        std::map<std::string, std::string> result_dict;

        // Iterate through all 'String' elements in the XAML file
        for (pugi::xml_node string_element : doc.select_nodes("//String")) {
            const char* key = string_element.attribute("Key").value();
            if (key != nullptr && *key != '\0') {
                const char* text = string_element.child_value();
                if (text == nullptr || *text == '\0') {
                    result_dict[key] = "";
                } else {
                    result_dict[key] = text;
                }
            }
        }

        return result_dict;

    } catch (const pugi::xml_parse_error& e) {
        std::cerr << "Error parsing the XAML file: " << e.description() << std::endl;
        return {};
    }
}

int main() {
    std::string xaml_file = "path/to/your/xaml/file.xaml";
    auto result = parse_xaml_to_dict(xaml_file);

    for (const auto& pair : result) {
        std::cout << "Key: " << pair.first << ", Value: " << pair.second << std::endl;
    }

    return 0;
}