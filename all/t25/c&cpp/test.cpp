#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include <catch2/catch.hpp>
#include <nlohmann/json.hpp>
#include <fstream>
#include <cstdio>
#include <vector>
#include <string>
#include <iostream>

// Function signature for the function you want to test
void classify_json_objects_by_pid(const std::string &source_file, const std::vector<std::string> &pid_list, const std::string &match_file, const std::string &mismatch_file);

// Helper function for creating temporary files
std::string create_temp_file(const std::string &content) {
    char filename[] = "/tmp/tempfileXXXXXX";
    int fd = mkstemp(filename);
    if (fd == -1) {
        throw std::runtime_error("Could not create temporary file.");
    }
    close(fd);

    std::ofstream file(filename);
    file << content;
    file.close();

    return std::string(filename);
}

TEST_CASE("classify_json_objects_by_pid all match", "[classify]") {
    // Sample data
    nlohmann::json data = R"([
        {"name": "Alice", "pid": 1},
        {"name": "Bob", "pid": 2},
        {"name": "Charlie", "pid": 3}
    ])"_json;
    
    // Convert JSON to string for file writing
    const std::string json_content = data.dump(4);

    std::string source_file = create_temp_file(json_content);
    std::string match_file = create_temp_file("");
    std::string mismatch_file = create_temp_file("");

    std::vector<std::string> pid_list = {"1", "2", "3"};
    classify_json_objects_by_pid(source_file, pid_list, match_file, mismatch_file);

    // Verify match file content
    std::ifstream match_in(match_file);
    nlohmann::json matches;
    match_in >> matches;

    // Verify mismatch file content
    std::ifstream mismatch_in(mismatch_file);
    nlohmann::json mismatches;
    mismatch_in >> mismatches;

    REQUIRE(matches.size() == 3);
    REQUIRE(mismatches.size() == 0);

    // Clean up
    std::remove(source_file.c_str());
    std::remove(match_file.c_str());
    std::remove(mismatch_file.c_str());
}

TEST_CASE("classify_json_objects_by_pid no match", "[classify]") {
    // Sample data
    nlohmann::json data = R"([
        {"name": "Alice", "pid": 1},
        {"name": "Bob", "pid": 2},
        {"name": "Charlie", "pid": 3}
    ])"_json;

    // Convert JSON to string for file writing
    const std::string json_content = data.dump(4);

    std::string source_file = create_temp_file(json_content);
    std::string match_file = create_temp_file("");
    std::string mismatch_file = create_temp_file("");

    std::vector<std::string> pid_list = {"4", "5"};
    classify_json_objects_by_pid(source_file, pid_list, match_file, mismatch_file);

    // Verify match file content
    std::ifstream match_in(match_file);
    nlohmann::json matches;
    match_in >> matches;

    // Verify mismatch file content
    std::ifstream mismatch_in(mismatch_file);
    nlohmann::json mismatches;
    mismatch_in >> mismatches;

    REQUIRE(matches.size() == 0);
    REQUIRE(mismatches.size() == 3);

    // Clean up
    std::remove(source_file.c_str());
    std::remove(match_file.c_str());
    std::remove(mismatch_file.c_str());
}

TEST_CASE("classify_json_objects_by_pid partial match", "[classify]") {
    // Sample data
    nlohmann::json data = R"([
        {"name": "Alice", "pid": 1},
        {"name": "Bob", "pid": 2},
        {"name": "Charlie", "pid": 3}
    ])"_json;

    // Convert JSON to string for file writing
    const std::string json_content = data.dump(4);

    std::string source_file = create_temp_file(json_content);
    std::string match_file = create_temp_file("");
    std::string mismatch_file = create_temp_file("");

    std::vector<std::string> pid_list = {"1", "3"};
    classify_json_objects_by_pid(source_file, pid_list, match_file, mismatch_file);

    // Verify match file content
    std::ifstream match_in(match_file);
    nlohmann::json matches;
    match_in >> matches;

    // Verify mismatch file content
    std::ifstream mismatch_in(mismatch_file);
    nlohmann::json mismatches;
    mismatch_in >> mismatches;

    REQUIRE(matches.size() == 2);
    REQUIRE(mismatches.size() == 1);

    // Clean up
    std::remove(source_file.c_str());
    std::remove(match_file.c_str());
    std::remove(mismatch_file.c_str());
}

TEST_CASE("classify_json_objects_by_pid empty pid list", "[classify]") {
    // Sample data
    nlohmann::json data = R"([
        {"name": "Alice", "pid": 1},
        {"name": "Bob", "pid": 2},
        {"name": "Charlie", "pid": 3}
    ])"_json;

    // Convert JSON to string for file writing
    const std::string json_content = data.dump(4);

    std::string source_file = create_temp_file(json_content);
    std::string match_file = create_temp_file("");
    std::string mismatch_file = create_temp_file("");

    std::vector<std::string> pid_list = {};
    classify_json_objects_by_pid(source_file, pid_list, match_file, mismatch_file);

    // Verify match file content
    std::ifstream match_in(match_file);
    nlohmann::json matches;
    match_in >> matches;

    // Verify mismatch file content
    std::ifstream mismatch_in(mismatch_file);
    nlohmann::json mismatches;
    mismatch_in >> mismatches;

    REQUIRE(matches.size() == 0);
    REQUIRE(mismatches.size() == 3);

    // Clean up
    std::remove(source_file.c_str());
    std::remove(match_file.c_str());
    std::remove(mismatch_file.c_str());
}