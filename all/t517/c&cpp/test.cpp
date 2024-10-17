#include <catch2/catch_test_macros.hpp>
#include <fstream>
#include <vector>
#include <nlohmann/json.hpp>
#include <filesystem>

namespace fs = std::filesystem;

using json = nlohmann::json;
using json_list = std::vector<json>;

TEST_CASE("Test reading JSON Lines files", "[jsonl]") {
    // Create temporary JSON Lines files for testing
    const std::string valid_jsonl_file = "test_valid.jsonl";
    const std::string invalid_jsonl_file = "test_invalid.jsonl";
    const std::string non_existent_file = "non_existent.jsonl";
    const std::string empty_jsonl_file = "test_empty.jsonl";

    // Valid JSON Lines content
    {
        std::ofstream file(valid_jsonl_file);
        file << R"({"name": "Alice", "age": 30})\n";
        file << R"({"name": "Bob", "age": 25})\n";
        file << R"({"name": "Charlie", "age": 35})\n";
    }

    // Invalid JSON Lines content
    {
        std::ofstream file(invalid_jsonl_file);
        file << R"({"name": "Alice", "age": 30})\n";
        file << R"({"name": "Bob", "age": "twenty-five}\n");  // Missing closing quote
    }

    // Empty JSON Lines file
    {
        std::ofstream file(empty_jsonl_file);
        file << "";  // Create an empty JSON Lines file
    }

    SECTION("Test reading a valid JSON Lines file") {
        json_list expected_data = {
            json{{"name", "Alice"}, {"age", 30}},
            json{{"name", "Bob"}, {"age", 25}},
            json{{"name", "Charlie"}, {"age", 35}}
        };

        json_list result = read_jsonl(valid_jsonl_file);
        REQUIRE(result == expected_data);
    }

    SECTION("Test for FileNotFoundError when the file does not exist") {
        REQUIRE_THROWS_AS(read_jsonl(non_existent_file), std::runtime_error);
    }

    SECTION("Test reading an empty JSON Lines file") {
        json_list result = read_jsonl(empty_jsonl_file);
        REQUIRE(result.empty());
    }

    // Remove the temporary JSON Lines files after testing
    if (fs::exists(valid_jsonl_file)) {
        fs::remove(valid_jsonl_file);
    }
    if (fs::exists(invalid_jsonl_file)) {
        fs::remove(invalid_jsonl_file);
    }
    if (fs::exists(empty_jsonl_file)) {
        fs::remove(empty_jsonl_file);
    }
}