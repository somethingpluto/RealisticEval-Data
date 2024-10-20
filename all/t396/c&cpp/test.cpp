TEST_CASE("Test Length of LIS", "[LIS]") {
    SECTION("Empty list") {
        REQUIRE(length_of_LIS({}) == 0);
    }

    SECTION("Single element") {
        REQUIRE(length_of_lis({7}) == 1);
    }

    SECTION("Strictly increasing sequence") {
        REQUIRE(length_of_lis({1, 2, 3, 4, 5}) == 5);
    }

    SECTION("Strictly decreasing sequence") {
        REQUIRE(length_of_lis({5, 4, 3, 2, 1}) == 1);
    }

    SECTION("Complex sequence") {
        REQUIRE(length_of_lis({10, 9, 2, 5, 3, 7, 101, 18}) == 4);
    }

    SECTION("All equal elements") {
        REQUIRE(length_of_lis({2, 2, 2, 2}) == 1);
    }

    SECTION("With negative numbers") {
        REQUIRE(length_of_lis({-1, -2, -3, 0, 1, 2}) == 4);
    }
}