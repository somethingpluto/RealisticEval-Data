#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <string>
#include <pugixml.hpp>

// Function to convert an XML file into a vector of maps
std::vector<std::map<std::string, std::string>> xml_to_vector_of_maps(const std::string& xml_file) {
    // Parse the XML file
    pugi::xml_document doc;
    if (!doc.load_file(xml_file.c_str())) {
        std::cerr << "Failed to load XML file: " << xml_file << std::endl;
        return {};
    }

    // Prepare a vector to hold all rows
    std::vector<std::map<std::string, std::string>> rows;

    // Iterate over each <sequence> element in the XML file
    for (pugi::xml_node sequence : doc.child("root").children("sequence")) {
        std::map<std::string, std::string> row_data;

        // Iterate over each child of the <sequence> element
        for (pugi::xml_node child : sequence.children()) {
            // Use the tag as the column name and the text content as the value
            row_data[child.name()] = child.text().get();
        }

        rows.push_back(row_data);
    }

    return rows;
}

int main() {
    std::string xml_file = "example.xml";  // Replace with the path to your XML file

    // Convert the XML file into a vector of maps
    std::vector<std::map<std::string, std::string>> data = xml_to_vector_of_maps(xml_file);

    // Print the data
    for (const auto& row : data) {
        for (const auto& entry : row) {
            std::cout << entry.first << ": " << entry.second << std::endl;
        }
        std::cout << "-----------------" << std::endl;
    }

    return 0;
}