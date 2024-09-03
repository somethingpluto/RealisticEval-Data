#define CATCH_CONFIG_MAIN
#include "../../lib/catch.hpp"
#include "../adapted.cpp"
// Test function for iterative, recursive, and memoization Fibonacci
TEST_CASE("Fibonacci sequence", "[fibonacci]") {
    // Test Case 1: Fibonacci of 0
    SECTION("Fibonacci(0) should be 0") {
        REQUIRE(fibonacciRecursive(0) == 0);
    }

    // Test Case 2: Fibonacci of 1
    SECTION("Fibonacci(1) should be 1") {
        REQUIRE(fibonacciRecursive(1) == 1);
    }

    // Test Case 3: Fibonacci of 5
    SECTION("Fibonacci(5) should be 5") {
        REQUIRE(fibonacciRecursive(5) == 5);
    }

    // Test Case 4: Fibonacci of 10
    SECTION("Fibonacci(10) should be 55") {
        REQUIRE(fibonacciRecursive(10) == 55);
    }

    // Test Case 5: Fibonacci of 20
    SECTION("Fibonacci(20) should be 6765") {
        REQUIRE(fibonacciRecursive(20) == 6765);
    }
}