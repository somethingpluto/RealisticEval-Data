#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>
#include <string>

// Assuming the compressString function is defined here or included.

TEST_CASE("compressString", "[compressString]") {

    SECTION("should return the original string if it is shorter than the max length") {
        std::string input = "Short string";
        std::string result = compressString(input);
        REQUIRE(result == input);
    }

    SECTION("should return the original string if it is exactly equal to the max length") {
        std::string input = "Exactly 18 chars";
        std::string result = compressString(input);
        REQUIRE(result == input);
    }

    SECTION("should truncate the string and append '...' if it exceeds the max length") {
        std::string input = "This is a long string that needs to be compressed.";
        std::string result = compressString(input);
        REQUIRE(result == "This is a long ...");
    }

    SECTION("should truncate the string to maxLength - 3 and append '...' when maxLength is specified") {
        std::string input = "Another long string that is definitely too long.";
        std::string result = compressString(input, 25);
        REQUIRE(result == "Another long string th...");
    }

    SECTION("should use default max length of 18 if no maxLength is provided") {
        std::string input = "This string is way too long.";
        std::string result = compressString(input);
        REQUIRE(result == "This string is ...");
    }

    SECTION("should return the original string if it is empty") {
        std::string input = "";
        std::string result = compressString(input);
        REQUIRE(result == input);
    }
}