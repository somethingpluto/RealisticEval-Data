TEST_CASE("Test point in polygon", "[point_in_polygon]") {
    // Define some polygons to use in tests
    std::vector<std::pair<double, double>> square = {{0, 0}, {0, 10}, {10, 10}, {10, 0}};
    std::vector<std::pair<double, double>> triangle = {{0, 0}, {5, 10}, {10, 0}};
    std::vector<std::pair<double, double>> concave = {{0, 0}, {5, 5}, {10, 0}, {5, 10}, {0, 10}};

    SECTION("Point inside the square") {
        REQUIRE(is_point_in_polygon({5, 5}, square));
    }

    SECTION("Point outside the square") {
        REQUIRE_FALSE(is_point_in_polygon({15, 5}, square));
    }

    SECTION("Point on the edge of the triangle") {
        REQUIRE_FALSE(is_point_in_polygon({5, 0}, triangle));
    }

    SECTION("Point inside concave polygon") {
        REQUIRE(is_point_in_polygon({5, 9}, concave));
    }

    SECTION("Point outside concave polygon") {
        REQUIRE_FALSE(is_point_in_polygon({5, 1}, concave));
    }
}