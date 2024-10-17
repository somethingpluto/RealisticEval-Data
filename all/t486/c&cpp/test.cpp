include <catch2/catch_test_macros.hpp>
#include <catch2/generators/catch_generators_all.hpp>
#include <stdexcept>

// Test fixture for Calculator
TEST_CASE("Calculator operations", "[Calculator]") {
    Calculator calculator;

    // Test the addition method.
    SECTION("Addition") {
        float result = calculator.add(10, 5);
        REQUIRE(result == 15);
    }

    // Test the subtraction method.
    SECTION("Subtraction") {
        float result = calculator.subtract(10, 5);
        REQUIRE(result == 5);
    }

    // Test the multiplication method.
    SECTION("Multiplication") {
        float result = calculator.multiply(10, 5);
        REQUIRE(result == 50);
    }

    // Test the division method.
    SECTION("Division") {
        float result = calculator.divide(10, 5);
        REQUIRE(result == 2.0f);
    }

    // Test division by zero raises std::invalid_argument.
    SECTION("Division by zero") {
        REQUIRE_THROWS_AS(calculator.divide(10, 0), std::invalid_argument);
    }
}