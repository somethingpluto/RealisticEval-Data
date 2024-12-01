bool approximately_equal(double a, double b, double epsilon = 1e-9) {
    return std::abs(a - b) < epsilon;
}

TEST_CASE("Calculate Bearing Tests", "[calculate_bearing]") {
    SECTION("North Bearing") {
        // From equator directly north
        REQUIRE(approximately_equal(calculate_bearing(0, 0, 10, 0), 0));
    }

    SECTION("East Bearing") {
        // From prime meridian directly east
        REQUIRE(approximately_equal(calculate_bearing(0, 0, 0, 10), 90));
    }

    SECTION("South Bearing") {
        // From a point directly south
        REQUIRE(approximately_equal(calculate_bearing(10, 0, 0, 0), 180));
    }

    SECTION("West Bearing") {
        // From a point directly west
        REQUIRE(approximately_equal(calculate_bearing(0, 10, 0, 0), 270));
    }

    SECTION("Across Prime Meridian") {
        // From a point west of the prime meridian to a point east
        REQUIRE(approximately_equal(calculate_bearing(0, -1, 0, 1), 90));
    }
}
