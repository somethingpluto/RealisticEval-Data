#define CATCH_CONFIG_MAIN

#include "../lib/catch.hpp"

int Factorial(int number) {
    return number <= 1 ? 1 : Factorial(number - 1) * number;
}

TEST_CASE("AAAA", "[single-file]") {
    REQUIRE(Factorial(1) == 1);
}