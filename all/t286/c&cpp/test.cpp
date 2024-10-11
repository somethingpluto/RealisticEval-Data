TEST_CASE("Find Largest Divisible", "[find_largest_divisible]") {
    SECTION("n is less than 5") {
        REQUIRE(find_largest_divisible(4) == nullptr);
    }

    SECTION("n is exactly 5") {
        REQUIRE(find_largest_divisible(5) == 5);
    }

    SECTION("n is between 5 and 10") {
        REQUIRE(find_largest_divisible(7) == 5);
    }

    SECTION("n is between 10 and 15") {
        REQUIRE(find_largest_divisible(13) == 10);
    }

    SECTION("n is exactly 10") {
        REQUIRE(find_largest_divisible(10) == 10);
    }

    SECTION("n is between 15 and 20") {
        REQUIRE(find_largest_divisible(18) == 15);
    }

    SECTION("n is between 20 and 25") {
        REQUIRE(find_largest_divisible(23) == 20);
    }

    SECTION("n is exactly 25") {
        REQUIRE(find_largest_divisible(25) == 25);
    }

    SECTION("n is greater than 25") {
        REQUIRE(find_largest_divisible(30) == 25);
    }
}