#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>
#include <string>
#include "your_module.h"  // Assuming the function is implemented in a header or source named your_module

TEST_CASE("Test equal length strings", "[stringSideBySide]") {
    std::string str1 = "Hello\nWorld";
    std::string str2 = "Python\nCode";
    std::string result = stringSideBySide(str1, str2);
    std::string expected = "Hello                | Python              \nWorld                | Code                ";
    REQUIRE(result == expected);
}

TEST_CASE("Test first string longer", "[stringSideBySide]") {
    std::string str1 = "Hello\nWorld\nTest";
    std::string str2 = "Python\nCode";
    std::string result = stringSideBySide(str1, str2);
    std::string expected = "Hello                | Python              \nWorld                | Code                \nTest                 |                     ";
    REQUIRE(result == expected);
}

TEST_CASE("Test second string longer", "[stringSideBySide]") {
    std::string str1 = "Hello\nWorld";
    std::string str2 = "Python\nCode\nTest";
    std::string result = stringSideBySide(str1, str2);
    std::string expected = "Hello                | Python              \nWorld                | Code                \n                     | Test                ";
    REQUIRE(result == expected);
}

TEST_CASE("Test empty first string", "[stringSideBySide]") {
    std::string str1 = "";
    std::string str2 = "Python\nCode";
    std::string result = stringSideBySide(str1, str2);
    std::string expected = "                     | Python              \n                     | Code                ";
    REQUIRE(result == expected);
}

TEST_CASE("Test custom column width", "[stringSideBySide]") {
    std::string str1 = "Hello\nWorld";
    std::string str2 = "Python\nCode";
    std::string result = stringSideBySide(str1, str2, 10);
    std::string expected = "Hello      | Python    \nWorld      | Code      ";
    REQUIRE(result == expected);
}