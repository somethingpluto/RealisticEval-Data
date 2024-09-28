#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <tinyxml2.h>

using namespace tinyxml2;

std::vector<std::map<std::string, std::string>> xml_to_data(const std::string& xml_file) {
    std::vector<std::map<std::string, std::string>> rows;

    XMLDocument doc;
    if (doc.LoadFile(xml_file.c_str()) != XML_SUCCESS) {
        std::cerr << "Error loading XML file" << std::endl;
        return rows;
    }

    XMLElement* root = doc.RootElement();
    if (!root) {
        std::cerr << "Error finding root element" << std::endl;
        return rows;
    }

    for (XMLElement* sequence = root->FirstChildElement("sequence"); sequence != nullptr; sequence = sequence->NextSiblingElement("sequence")) {
        std::map<std::string, std::string> row_data;

        for (XMLElement* child = sequence->FirstChildElement(); child != nullptr; child = child->NextSiblingElement()) {
            row_data[child->Name()] = child->GetText() ? child->GetText() : "";
        }

        rows.push_back(row_data);
    }

    return rows;
}

int main() {
    std::string xml_file = "path_to_your_xml_file.xml"; // replace with your XML file path
    std::vector<std::map<std::string, std::string>> data = xml_to_data(xml_file);

    // Printing the data to verify
    for (const auto& row : data) {
        for (const auto& [key, value] : row) {
            std::cout << key << ": " << value << ", ";
        }
        std::cout << std::endl;
    }

    return 0;
}