TEST_CASE("Sum Function Tests") {
    SECTION("should return the sum of a normal array of positive numbers") {
        REQUIRE(sum({1, 2, 3, 4, 5}) == 15);
    }

    SECTION("should return the sum of an array containing negative numbers") {
        REQUIRE(sum({-1, -2, -3, -4, -5}) == -15);
    }

    SECTION("should return 0 for an empty array") {
        REQUIRE(sum({}) == 0);
    }

    SECTION("should return the sum of an array containing both positive and negative numbers") {
        REQUIRE(sum({10, -10, 5, -5, 15}) == 15);
    }

    SECTION("should return the sum of an array with floating point numbers") {
        REQUIRE(sum({1.5, 2.5, 3.5}) == Approx(7.5)); // Using Approx for floating-point comparison
    }
}