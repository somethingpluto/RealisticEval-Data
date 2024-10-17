#include <catch2/catch_test_macros.hpp>
#include <string>
#include <sstream>
#include <vector>

TEST_CASE("Test basic snake_case to CamelCase conversion", "[snake_to_camel]") {
    CHECK(snake_to_camel("hello_world") == "HelloWorld");
}

TEST_CASE("Test conversion of a snake_case string with multiple words", "[snake_to_camel]") {
    CHECK(snake_to_camel("this_is_a_test") == "ThisIsATest");
}

TEST_CASE("Test conversion with numbers in the string", "[snake_to_camel]") {
    CHECK(snake_to_camel("convert_this_123_string") == "ConvertThis123String");
}

TEST_CASE("Test conversion with leading and trailing underscores", "[snake_to_camel]") {
    CHECK(snake_to_camel("_leading_and_trailing_") == "LeadingAndTrailing");
    CHECK(snake_to_camel("___multiple___underscores___") == "MultipleUnderscores");
}

TEST_CASE("Test conversion of an empty string", "[snake_to_camel]") {
    CHECK(snake_to_camel("") == "");
}