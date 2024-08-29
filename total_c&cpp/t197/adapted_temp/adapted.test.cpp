#define CATCH_CONFIG_MAIN
#include "../../lib/catch.hpp"
#include "../adapted.cpp"
TEST_CASE("FindOrder Test Cases", "[findOrder]") {
    // Test Case 1: Minimum valid input with 2 players
    REQUIRE(findOrder(2) == vector<int>{2, 1});

    // Test Case 2: 3 players
    REQUIRE(findOrder(3) == vector<int>{2, 3, 1});

    // Test Case 3: 5 players
    REQUIRE(findOrder(5) == vector<int>{2, 5, 4, 1, 3});

    // Test Case 4: 7 players
    REQUIRE(findOrder(7) == vector<int>{2, 5, 1, 6, 4, 7, 3});

    // Test Case 5: 10 players
    REQUIRE(findOrder(10) == vector<int>{2, 5, 8, 1, 6, 4, 7, 10, 3, 9});
}