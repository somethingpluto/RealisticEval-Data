#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <exception>
#include <difflib.h> // Note: difflib.h is not a standard C++ library. You may need to implement or find an equivalent library.

std::vector<std::string> compare_files(const std::string& file1_path, const std::string& file2_path) {
    /**
     * Compare the contents of two files and print the differences in unified diff format.
     *
     * Args:
     * file1_path (const std::string&): Path to the first file.
     * file2_path (const std::string&): Path to the second file.
     *
     * Returns:
     * std::vector<std::string>: A vector containing the lines of differences, if any.
     *
     * Throws:
     * std::runtime_error: If either file does not exist or there is an error reading the files.
     */
    std::ifstream file1(file1_path);
    std::ifstream file2(file2_path);

    if (!file1.is_open()) {
        throw std::runtime_error("One of the files was not found.");
    }

    if (!file2.is_open()) {
        throw std::runtime_error("One of the files was not found.");
    }

    std::vector<std::string> lines1;
    std::vector<std::string> lines2;

    std::string line;
    while (std::getline(file1, line)) {
        lines1.push_back(line);
    }

    while (std::getline(file2, line)) {
        lines2.push_back(line);
    }

    file1.close();
    file2.close();

    std::vector<std::string> diff_lines;
    std::vector<char*> diff = unified_diff(lines1, lines2, file1_path.c_str(), file2_path.c_str());

    for (auto& diff_line : diff) {
        std::cout << diff_line << std::endl;
        diff_lines.push_back(diff_line);
    }

    return diff_lines;
}

int main() {
    try {
        std::vector<std::string> diff_lines = compare_files("file1.txt", "file2.txt");
    } catch (const std::exception& e) {
        std::cerr << "Exception: " << e.what() << std::endl;
    }

    return 0;
}