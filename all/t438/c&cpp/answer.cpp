#include <iostream>
#include <string>
#include <csv.h> // Assuming you have installed the cppcsv library

// Function to read a CSV file and convert it to a structured format
void read_csv_to_structured_format(const std::string& file_path) {
    try {
        csv::Parser file = csv::Parser(file_path);

        if (file.is_open()) {
            // Print header
            for (const auto& header : file.headers()) {
                std::cout << header << " ";
            }
            std::cout << "\n";

            // Print rows
            for (const auto& row : file) {
                for (const auto& cell : row) {
                    std::cout << cell << " ";
                }
                std::cout << "\n";
            }
        } else {
            std::cout << "Error: The file '" << file_path << "' could not be opened.\n";
        }
    } catch (const std::exception& e) {
        std::cout << "An error occurred: " << e.what() << "\n";
    }
}