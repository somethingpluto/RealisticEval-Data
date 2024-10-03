#define CATCH_CONFIG_MAIN
#include "./lib/catch.hpp"
#include "./solution.cpp"
// Test cases
TEST_CASE("Count words in various strings") {
    SECTION("Empty string") {
        REQUIRE(countWords("") == 0);
    }

    SECTION("String with only spaces") {
        REQUIRE(countWords("     ") == 0);
    }

    SECTION("Single word") {
        REQUIRE(countWords("Hello") == 1);
    }

    SECTION("Multiple words with single spaces") {
        REQUIRE(countWords("This is a test string") == 5);
    }

    SECTION("Multiple spaces between words") {
        REQUIRE(countWords("This    is   a   test   string") == 5);
    }

    SECTION("Leading and trailing spaces") {
        REQUIRE(countWords("   Hello world!   ") == 2);
    }
}