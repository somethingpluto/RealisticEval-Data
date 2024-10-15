TEST_CASE("getArrayAverage") {
    SECTION("should return the average of an array of positive integers") {
        REQUIRE(getArrayAverage({1, 2, 3, 4, 5}) == Approx(3)); // (1 + 2 + 3 + 4 + 5) / 5 = 3
    }

    SECTION("should return the average of an array with negative numbers") {
        REQUIRE(getArrayAverage({-1, -2, -3, -4, -5}) == Approx(-3)); // (-1 + -2 + -3 + -4 + -5) / 5 = -3
    }

    SECTION("should return the average of an array with mixed positive and negative numbers") {
        REQUIRE(getArrayAverage({1, -1, 2, -2, 3, -3}) == Approx(0)); // (1 + -1 + 2 + -2 + 3 + -3) / 6 = 0
    }

    SECTION("should handle an empty array (edge case)") {
        REQUIRE(std::isnan(getArrayAverage({}))); // Division by zero, expected result is NaN
    }

    SECTION("should return the single element when the array contains one item") {
        REQUIRE(getArrayAverage({7}) == Approx(7)); // The average of [7] is 7
    }
}