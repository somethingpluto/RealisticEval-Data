TEST_CASE("Test cases for min_removals_to_make_unique", "[min_removals_to_make_unique]") {
    SECTION("Test with a basic array where multiple removals are needed") {
        REQUIRE(min_removals_to_make_unique({3, 3, 1, 2, 2, 1}) == 3);
    }

    SECTION("Test an array where all elements are identical") {
        REQUIRE(min_removals_to_make_unique({4, 4, 4, 4}) == 3);
    }

    SECTION("Test an array where all elements are already unique") {
        REQUIRE(min_removals_to_make_unique({1, 2, 3, 4}) == 0);
    }

    SECTION("Test an empty array") {
        REQUIRE(min_removals_to_make_unique({}) == 0);
    }

    SECTION("Test a more complex case with a larger array") {
        REQUIRE(min_removals_to_make_unique({1, 2, 2, 3, 3, 3, 4, 4, 4, 4}) == 6);
    }
}