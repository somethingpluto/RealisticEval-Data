#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>
#include <fstream>
#include <filesystem>
#include "find_json_files_with_keyword.hpp"  // include the header file for your function

namespace fs = std::filesystem;

TEST_CASE("find_json_files_with_keyword") {
    fs::path test_dir = fs::temp_directory_path() / fs::unique_path();
    fs::create_directory(test_dir);

    auto write_to_file = [](const fs::path &path, const std::string &content) {
        std::ofstream file(path);
        file << content;
        file.close();
    };

    SECTION("keyword in single file") {
        fs::path test_file_path = test_dir / "test.js.json";
        write_to_file(test_file_path, R"({"key": "value with keyword"})");
        
        std::vector<std::string> result = find_json_files_with_keyword(test_dir.string(), "keyword");
        std::vector<std::string> expected = {test_file_path.string()};

        REQUIRE(result == expected);
    }

    SECTION("keyword not in file") {
        fs::path test_file_path = test_dir / "test.js.json";
        write_to_file(test_file_path, R"({"key": "no keyword here"})");
        
        std::vector<std::string> result = find_json_files_with_keyword(test_dir.string(), "wc");
        std::vector<std::string> expected;

        REQUIRE(result == expected);
    }

    SECTION("no json files in directory") {
        std::vector<std::string> result = find_json_files_with_keyword(test_dir.string(), "keyword");
        std::vector<std::string> expected;

        REQUIRE(result == expected);
    }

    SECTION("multiple json files") {
        fs::path file1_path = test_dir / "file1.json";
        fs::path file2_path = test_dir / "file2.json";
        write_to_file(file1_path, R"({"key": "keyword present here"})");
        write_to_file(file2_path, R"({"key": "keyword present here"})");

        std::vector<std::string> result = find_json_files_with_keyword(test_dir.string(), "keyword");
        std::vector<std::string> expected = {file1_path.string(), file2_path.string()};

        REQUIRE(result == expected);
    }

    // Cleanup after test
    fs::remove_all(test_dir);
}