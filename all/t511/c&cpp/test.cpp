#include <catch2/catch_test_macros.hpp>
#include <string>
#include <stdexcept>


TEST_CASE("Test valid hex color inputs", "[hex_to_ansi]") {
    SECTION("Valid colors") {
        CHECK(hex_to_ansi("#FF5733") == "\x1b[38;2;255;87;51m");
        CHECK(hex_to_ansi("#00FF00") == "\x1b[38;2;0;255;0m");
        CHECK(hex_to_ansi("#0000FF") == "\x1b[38;2;0;0;255m");
    }
}

TEST_CASE("Test edge cases with black and white colors", "[hex_to_ansi]") {
    SECTION("Black and white colors") {
        CHECK(hex_to_ansi("#000000") == "\x1b[38;2;0;0;0m");  // Black
        CHECK(hex_to_ansi("#FFFFFF") == "\x1b[38;2;255;255;255m");  // White
    }
}