#define CATCH_CONFIG_MAIN
#include "./lib/catch.hpp"
#include "./solution.cpp"
TEST_CASE("TestSmartConvert") {
    SECTION("test_convert_integer") {
        auto result = numerical_str_convert("123");
        REQUIRE(std::holds_alternative<int>(result));
        REQUIRE(std::get<int>(result) == 123);
    }

    SECTION("test_convert_float") {
        auto result = numerical_str_convert("123.45");
        REQUIRE(std::holds_alternative<double>(result));
        REQUIRE(std::get<double>(result) == 123.45);
    }

    SECTION("test_convert_non_numeric_string") {
        auto result = numerical_str_convert("abc");
        REQUIRE(std::holds_alternative<std::string>(result));
        REQUIRE(std::get<std::string>(result) == "abc");
    }

    SECTION("test_convert_negative_integer") {
        auto result = numerical_str_convert("-456");
        REQUIRE(std::holds_alternative<int>(result));
        REQUIRE(std::get<int>(result) == -456);
    }

    SECTION("test_convert_negative_float") {
        auto result = numerical_str_convert("-456.78");
        REQUIRE(std::holds_alternative<double>(result));
        REQUIRE(std::get<double>(result) == -456.78);
    }
}