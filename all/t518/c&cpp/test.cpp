#include <catch2/catch_test_macros.hpp>
#include <map>
#include <string>
#include <cctype>

TEST_CASE("TestConvertCsvValues", "[convertCsvValues]") {
    SECTION("test_valid_numeric_strings") {
        std::map<std::string, std::string> row = {
            {"value1", "1,234"},
            {"value2", "5,678"},
            {"value3", "9,876"}
        };
        std::map<std::string, std::string> expected = {
            {"value1", "1.234"},
            {"value2", "5.678"},
            {"value3", "9.876"}
        };
        auto result = convertCsvValues(row);
        REQUIRE(result == expected);
    }

    SECTION("test_non_numeric_strings") {
        std::map<std::string, std::string> row = {
            {"value1", "not_a_number"},
            {"value2", "hello"},
            {"value3", "world"}
        };
        std::map<std::string, std::string> expected = {
            {"value1", ""},
            {"value2", ""},
            {"value3", ""}
        };
        auto result = convertCsvValues(row);
        REQUIRE(result == expected);
    }

    SECTION("test_mixed_values") {
        std::map<std::string, std::string> row = {
            {"value1", "1,234"},
            {"value2", "not_a_number"},
            {"value3", "3,14159"}
        };
        std::map<std::string, std::string> expected = {
            {"value1", "1.234"},
            {"value2", ""},
            {"value3", "3.14159"}
        };
        auto result = convertCsvValues(row);
        REQUIRE(result == expected);
    }

    SECTION("test_no_values") {
        std::map<std::string, std::string> row = {
            {"value1", "aaaa"},
            {"value2", "not_a_number"},
            {"value3", "3,14"}
        };
        std::map<std::string, std::string> expected = {
            {"value1", ""},
            {"value2", ""},
            {"value3", "3.14"}
        };
        auto result = convertCsvValues(row);
        REQUIRE(result == expected);
    }

    SECTION("test_edge_cases") {
        std::map<std::string, std::string> row = {
            {"value1", ""},
            {"value2", "0.0"},
            {"value3", "1,23"}
        };
        std::map<std::string, std::string> expected = {
            {"value1", ""},
            {"value2", "0.0"},
            {"value3", "1.23"}
        };
        auto result = convertCsvValues(row);
        REQUIRE(result == expected);
    }
}