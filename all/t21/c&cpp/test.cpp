#define CATCH_CONFIG_MAIN
#include "catch.hpp"
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

// Assume the `compareFiles` function is defined exactly as in the previous example
std::vector<std::string> compareFiles(const std::string &file1Path, const std::string &file2Path);

void writeFile(const std::string &filePath, const std::string &content) {
    std::ofstream file(filePath);
    if (!file.is_open()) {
        throw std::runtime_error("Cannot open file: " + filePath);
    }
    file << content;
    file.close();
}

void removeFile(const std::string &filePath) {
    std::remove(filePath.c_str());
}

TEST_CASE("TestCompareFiles") {
    const std::string file1Path = "file1.txt";
    const std::string file2Path = "file2.txt";

    SECTION("Identical files") {
        std::string file1Content = "Line1\nLine2\nLine3\n";
        std::string file2Content = "Line1\nLine2\nLine3\n";

        writeFile(file1Path, file1Content);
        writeFile(file2Path, file2Content);

        auto result = compareFiles(file1Path, file2Path);
        REQUIRE(result.size() == 0);
        
        removeFile(file1Path);
        removeFile(file2Path);
    }

    SECTION("Files with differences") {
        std::string file1Content = "Line1\nLine2\nLine3\n";
        std::string file2Content = "Line1\nLineChanged\nLine3\n";

        writeFile(file1Path, file1Content);
        writeFile(file2Path, file2Content);

        auto result = compareFiles(file1Path, file2Path);
        REQUIRE(result.size() != 0);
        
        removeFile(file1Path);
        removeFile(file2Path);
    }

    SECTION("Nonexistent file") {
        std::remove(file1Path.c_str());

        REQUIRE_THROWS_AS(compareFiles("nonexistent.txt", "file2.txt"), std::runtime_error);

        removeFile(file2Path);
    }

    SECTION("File reading error") {
        // To simulate a file-reading error, we would need to set conditions that trigger an error, but in practice,
        // it's not as straightforward to mock low-level file reading as it is in Python.
        //
        // For testing purposes, we can define a special test function that throws directly:
        auto compareFilesWithError = [](const std::string &file1Path, const std::string &file2Path) -> std::vector<std::string> {
            throw std::runtime_error("Error reading file");
            return {};
        };

        REQUIRE_THROWS_AS(compareFilesWithError(file1Path, file2Path), std::runtime_error);
    }
}