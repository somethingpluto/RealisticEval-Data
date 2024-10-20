TEST_CASE("Test Decompose Function", "[decompose]") {
    SECTION("Edge case with larger shape") {
        REQUIRE(decompose(60, {4, 4, 4}) == std::make_tuple(3, 3, 0));
    }

    SECTION("Last valid index") {
        REQUIRE(decompose(63, {4, 4, 4}) == std::make_tuple(3, 3, 3));
    }

    SECTION("Single dimension case") {
        REQUIRE(decompose(2, {5}) == std::make_tuple(2));
    }

    SECTION("Invalid cases") {
        // Test case 5: Out of bounds case (negative index)
        REQUIRE_THROWS_AS(decompose(-1, {3, 4, 5}), std::out_of_range);

        // Test case 6: Out of bounds case (index too large)
        REQUIRE_THROWS_AS(decompose(100, {3, 4, 5}), std::out_of_range);
    }
}