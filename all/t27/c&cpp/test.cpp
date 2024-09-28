#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>
#include <json/json.h>
#include <filesystem>
#include <fstream>
#include <vector>

namespace fs = std::filesystem;

// Function prototype for concatenateJsonArrays
std::vector<Json::Value> concatenateJsonArrays(const std::string &directory);

// Helper function to create test JSON files
void createTestFile(const std::string &filename, const Json::Value &content) {
    std::ofstream file(filename);
    file << content;
}

// Test suite for concatenateJsonArrays
TEST_CASE("TestConcatenateJsonArrays", "[json]") {
    std::string testDir = "test_json";
    fs::create_directory(testDir);

    // Set up test files
    createTestFile(testDir + "/array1.json", Json::Value(Json::arrayValue));
    createTestFile(testDir + "/array1.json")[0] = 1;
    createTestFile(testDir + "/array1.json")[1] = 2;
    createTestFile(testDir + "/array1.json")[2] = 3;

    createTestFile(testDir + "/array2.json", Json::Value(Json::arrayValue));
    createTestFile(testDir + "/array2.json")[0] = "a";
    createTestFile(testDir + "/array2.json")[1] = "b";
    createTestFile(testDir + "/array2.json")[2] = "c";

    createTestFile(testDir + "/not_array.json", Json::Value(Json::objectValue));
    createTestFile(testDir + "/not_array.json")["key"] = "value";

    createTestFile(testDir + "/empty.json", Json::Value(Json::arrayValue));

    std::ofstream nonJsonFile(testDir + "/non_json.txt");
    nonJsonFile << "This is not a JSON file.";
    nonJsonFile.close();

    // Test with valid JSON arrays
    SECTION("Concatenate valid JSON arrays") {
        auto result = concatenateJsonArrays(testDir);
        REQUIRE(result.size() == 5);
        REQUIRE(result[0].asInt() == 1);
        REQUIRE(result[1].asInt() == 2);
        REQUIRE(result[2].asInt() == 3);
        REQUIRE(result[3].asString() == "a");
        REQUIRE(result[4].asString() == "b");
        REQUIRE(result[5].asString() == "c");
    }

    // Test that non-array JSON files are ignored
    SECTION("Ignore non-array JSON") {
        auto result = concatenateJsonArrays(testDir);
        REQUIRE(result.size() == 5);
        REQUIRE_FALSE(std::any_of(result.begin(), result.end(), [](const Json::Value &val) {
            return val.isObject() && val.isMember("key");
        }));
    }

    // Test that non-JSON files are ignored
    SECTION("Ignore non-JSON files") {
        auto result = concatenateJsonArrays(testDir);
        REQUIRE_FALSE(std::any_of(result.begin(), result.end(), [](const Json::Value &val) {
            return val.asString() == "This is not a JSON file.";
        }));
    }

    // Test concatenation includes empty arrays
    SECTION("Handle empty arrays") {
        auto result = concatenateJsonArrays(testDir);
        REQUIRE(result.size() == 5);
        REQUIRE_FALSE(std::any_of(result.begin(), result.end(), [](const Json::Value &val) {
            return val.isArray() && val.empty();
        }));
    }

    // Clean up created files
    for (const auto &entry : fs::directory_iterator(testDir)) {
        fs::remove(entry.path());
    }
    fs::remove(testDir);
}

TEST_CASE("TestEmptyDirectory", "[json]") {
    std::string emptyDir = "empty_test_json";
    fs::create_directory(emptyDir);
    auto result = concatenateJsonArrays(emptyDir);
    REQUIRE(result.empty());
    fs::remove(emptyDir);
}