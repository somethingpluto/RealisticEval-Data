#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include "catch.hpp"
#include <string>

// Assuming the process_markdown function is defined elsewhere
std::string process_markdown(const std::string& s);

TEST_CASE("Tests for process_markdown function") {

    SECTION("Test single asterisk pair") {
        std::string content = "This is a *test.js* string.";
        std::string expected = "This is a *test.js* string.";
        REQUIRE(process_markdown(content) == expected);
    }

    SECTION("Test nested asterisks") {
        std::string content = "Example of **nested *asterisks***.";
        std::string expected = "Example of *nested asterisks*.";
        REQUIRE(process_markdown(content) == expected);
    }

    SECTION("Test multiple asterisk pairs") {
        std::string content = "*Multiple* pairs of *asterisks* in *one* sentence.";
        std::string expected = "*Multiple pairs of asterisks in one* sentence.";
        REQUIRE(process_markdown(content) == expected);
    }

    SECTION("Test asterisks with no text") {
        std::string content = "Asterisks with ** no text.";
        std::string expected = "Asterisks with ** no text.";
        REQUIRE(process_markdown(content) == expected);
    }

    SECTION("Test asterisks around spaces") {
        std::string content = "Asterisks around * *spaces* * are tricky.";
        std::string expected = "Asterisks around * spaces * are tricky.";
        REQUIRE(process_markdown(content) == expected);
    }
}