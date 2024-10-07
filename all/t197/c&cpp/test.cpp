TEST_CASE("FindOrder Test Cases", "[findOrder]") {
    // Test Case 1: Minimum valid input with 2 players
    REQUIRE(findOrder(2) == std::vector<int>{2, 1});

    // Test Case 2: 3 players
    REQUIRE(findOrder(3) == std::vector<int>{2, 3, 1});

    // Test Case 3: 5 players
    REQUIRE(findOrder(5) == std::vector<int>{2, 5, 3, 4, 1});

    // Test Case 4: 7 players
    REQUIRE(findOrder(7) == std::vector<int>{ 2, 5, 4, 1, 6, 7, 3});

    // Test Case 5: 10 players
    REQUIRE(findOrder(10) == std::vector<int>{ 2, 5, 10, 9, 7, 3, 4, 6, 8, 1});
}
