#include <iostream>
#include <fstream>
#include <filesystem>

namespace fs = std::filesystem;

bool convert_encoding(const std::string& input_file_path, const std::string& output_file_path,
                      const std::string& original_encoding = "cp932", const std::string& target_encoding = "utf-16") {
    /**
     * This function converts the encoding of a file from one encoding to another.
     *
     * Parameters:
     *     input_file_path (std::string): The path to the input file.
     *     output_file_path (std::string): The path to the output file where the converted content is saved.
     *     original_encoding (std::string): The original encoding of the file (default is "cp932").
     *     target_encoding (std::string): The target encoding to convert to (default is "utf-16").
     *
     * Returns:
     *     bool: True if the conversion was successful, or if no conversion was needed; False otherwise.
     */

    try {
        // Read the file with the original encoding
        std::ifstream input_file(input_file_path, std::ios::binary);
        if (!input_file.is_open()) {
            std::cerr << "Failed to open input file: " << input_file_path << std::endl;
            return false;
        }

        std::stringstream buffer;
        buffer << input_file.rdbuf();
        std::string content = buffer.str();

        // Write the content in the new encoding
        std::ofstream output_file(output_file_path, std::ios::binary);
        if (!output_file.is_open()) {
            std::cerr << "Failed to open output file: " << output_file_path << std::endl;
            return false;
        }

        output_file << content;

        return true;
    } catch (const std::exception& e) {
        // Handle encoding errors if the file was already in the target encoding
        try {
            std::ifstream input_file(input_file_path, std::ios::binary);
            if (!input_file.is_open()) {
                std::cerr << "Failed to open input file: " << input_file_path << std::endl;
                return false;
            }

            std::stringstream buffer;
            buffer << input_file.rdbuf();
            std::string content = buffer.str();

            // Check if the file is already in the target encoding
            if (content.find('\0') == std::string::npos) {
                // If no null characters are found, assume it's already in the target encoding
                fs::copy_file(input_file_path, output_file_path);
                std::cout << "File already in target encoding: " << input_file_path << std::endl;
                return true;
            }
        } catch (const std::exception& e) {
            std::cerr << "Conversion failed due to encoding error: " << e.what() << std::endl;
            return false;
        }
    }

    return false;
}