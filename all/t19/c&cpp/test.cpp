#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include <catch2/catch.hpp>
#include <string>
#include <regex>

bool contains_phone_number(const std::string& s) {
    // Regex pattern to identify phone numbers
    std::regex pattern(R"((\+\d{1,3}[- ]?)?(\d{3}[- ]\d{3}[- ]\d{4}))");

    // Use std::regex_search to find a match
    return std::regex_search(s, pattern);
}

TEST_CASE("Phone number detection tests") {
    SECTION("Test with international prefix") {
        REQUIRE(contains_phone_number("+1-800-555-1234"));
    }

    SECTION("Test with standard dashes") {
        REQUIRE(contains_phone_number("800-555-1234"));
    }

    SECTION("Test with spaces") {
        REQUIRE(contains_phone_number("800 555 1234"));
    }

    SECTION("Test without phone number") {
        REQUIRE_FALSE(contains_phone_number("Hello, world!"));
    }

    SECTION("Test with text containing numbers") {
        REQUIRE(contains_phone_number("Call me at 800-555-1234 today!"));
    }
}