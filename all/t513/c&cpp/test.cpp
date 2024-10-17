#include <catch2/catch_test_macros.hpp>
#include <string>
#include <cctype>
#include <regex>

TEST_CASE("Test is_phrase_in_string_ignore_case", "[is_phrase_in_string_ignore_case]") {
    SECTION("Exact match case insensitive") {
        REQUIRE(is_phrase_in_string_ignore_case("hello world", "Hello World"));
    }

    SECTION("Partial word match case insensitive") {
        REQUIRE(is_phrase_in_string_ignore_case("Hello", "saying Hello there"));
    }

    SECTION("Different cases") {
        REQUIRE(is_phrase_in_string_ignore_case("HELLO", "hello there!"));
        REQUIRE(is_phrase_in_string_ignore_case("world", "WORLD is great"));
    }

    SECTION("Non-existent phrase") {
        REQUIRE_FALSE(is_phrase_in_string_ignore_case("goodbye", "Hello world"));
        REQUIRE_FALSE(is_phrase_in_string_ignore_case("hello", "goodbye world"));
    }
}