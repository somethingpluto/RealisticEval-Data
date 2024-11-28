#include <iostream>
#include <fstream>
#include <vector>
#include <string>

void formatText(const std::string& input_file = "input.txt", const std::string& output_file = "output.txt") {
    try {
        // Open the input file in read mode
        std::ifstream input(input_file);
        if (!input.is_open()) {
            throw std::runtime_error("Input file not found.");
        }

        // Read the content of the input file line by line
        std::vector<std::string> lines;
        std::string line;
        while (std::getline(input, line)) {
            lines.push_back(line);
        }
        input.close();

        // Process each line
        std::vector<std::string> processed_lines;
        for (const auto& line : lines) {
            // Remove newline characters and add a space
            std::string processed_line = line;
            if (!processed_line.empty() && processed_line.back() == '\n') {
                processed_line.pop_back();
            }
            processed_lines.push_back(processed_line);  // Append the processed line
        }

        // Join the processed lines with spaces
        std::string content_without_newlines;
        for (size_t i = 0; i < processed_lines.size(); ++i) {
            content_without_newlines += processed_lines[i];
            if (i != processed_lines.size() - 1) {
                content_without_newlines += " ";
            }
        }

        // Open the output file in write mode
        std::ofstream output(output_file);
        if (!output.is_open()) {
            throw std::runtime_error("Output file could not be opened.");
        }

        // Write the content without newlines to the output file
        output << content_without_newlines;
        output.close();

        std::cout << "Line breaks removed and spaces added. Output written to " << output_file << std::endl;

    } catch (const std::exception& e) {
        std::cerr << e.what() << std::endl;
    }
}