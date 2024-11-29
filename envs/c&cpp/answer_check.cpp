#define CATCH_CONFIG_MAIN
#include "./lib/catch.hpp"
#include "./solution.cpp"
TEST_CASE("TestSanitizeData", "[SanitizeData]") {
    SECTION("test_empty_dict") {
        // Test with an empty dictionary.
        std::unordered_map<std::string, std::string> data = {};
        std::vector<std::string> key_to_remove = {"email", "metadata"};

        std::unordered_map<std::string, std::string> expected = {};
        REQUIRE(sanitize_data(data, &key_to_remove) == expected);
    }

    SECTION("test_remove_default_keys") {
        // Test removing default keys from a nested structure.
        std::unordered_map<std::string, std::string> data = {
            {"name", "John Doe"},
            {"email", "johndoe@example.com"},
            {"metadata", "version: 1, timestamp: 2021-07-10, status: pending"},
            {"comments", "Good, Needs review"}
        };
        std::vector<std::string> key_to_remove = {"email", "metadata"};
        std::unordered_map<std::string, std::string> expected = {
            {"name", "John Doe"},
            {"comments", "Good, Needs review"}
        };
        REQUIRE(sanitize_data(data, &key_to_remove) == expected);
    }

    SECTION("test_specified_key_to_remove") {
        // Test removing a specified key from the dictionary.
        std::unordered_map<std::string, std::string> data = {
            {"name", "John Doe"},
            {"location", "Earth"},
            {"email", "johndoe@example.com"}
        };
        std::unordered_map<std::string, std::string> expected = {
            {"name", "John Doe"},
            {"location", "Earth"}
        };
        REQUIRE(sanitize_data(data, &std::vector<std::string>{"email"}) == expected);
    }
}