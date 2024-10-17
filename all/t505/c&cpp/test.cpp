#include <catch2/catch_test_macros.hpp>
#include <string>
#include <regex>

TEST_CASE("Test CamelCase to snake_case conversion", "[camel_to_snake]") {
    SECTION("Basic conversion") {
        REQUIRE(camel_to_snake("HelloWorld") == "hello_world");
    }

    SECTION("Multiple words") {
        REQUIRE(camel_to_snake("ThisIsATest") == "this_is_a_test");
    }

    SECTION("With numbers") {
        REQUIRE(camel_to_snake("ConvertThis123String") == "convert_this123_string");
    }

    SECTION("Leading uppercase") {
        REQUIRE(camel_to_snake("PythonFunction") == "python_function");
    }

    SECTION("Empty string") {
        REQUIRE(camel_to_snake("") == "");
    }
}