#define CATCH_CONFIG_MAIN
#include "../../lib/catch.hpp"
#include "../original.cpp"

TEST_CASE("return_string Test Cases", "[return_string]") {
    // Test Case 1: Copy a non-empty string
    const char* original1 = "Hello, World!";
    char* copy1 = return_string(original1);
    REQUIRE(std::strcmp(copy1, original1) == 0);
    delete[] copy1;

    // Test Case 2: Copy an empty string
    const char* original2 = "";
    char* copy2 = return_string(original2);
    REQUIRE(std::strcmp(copy2, original2) == 0);
    delete[] copy2;

    // Test Case 3: Copy a string with special characters
    const char* original3 = "C++ is fun! @#$%^&*()";
    char* copy3 = return_string(original3);
    REQUIRE(std::strcmp(copy3, original3) == 0);
    delete[] copy3;

    // Test Case 4: Copy a single character string
    const char* original4 = "A";
    char* copy4 = return_string(original4);
    REQUIRE(std::strcmp(copy4, original4) == 0);
    delete[] copy4;

    // Test Case 5: Passing a null pointer (should throw an exception)
    REQUIRE_THROWS_AS(return_string(nullptr), std::invalid_argument);
}