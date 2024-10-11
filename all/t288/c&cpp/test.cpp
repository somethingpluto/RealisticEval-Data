TEST_CASE("Bresenham Line Algorithm", "[bresenham]") {
    SECTION("Line from (0, 0) to (3, 3)") {
        auto result = bresenham_line(0, 0, 3, 3);
        REQUIRE(result.size() == 4);
        CHECK(result[0] == std::make_pair(0, 0));
        CHECK(result[1] == std::make_pair(1, 1));
        CHECK(result[2] == std::make_pair(2, 2));
        CHECK(result[3] == std::make_pair(3, 3));
    }

    SECTION("Line from (0, 0) to (3, -3)") {
        auto result = bresenham_line(0, 0, 3, -3);
        REQUIRE(result.size() == 4);
        CHECK(result[0] == std::make_pair(0, 0));
        CHECK(result[1] == std::make_pair(1, -1));
        CHECK(result[2] == std::make_pair(2, -2));
        CHECK(result[3] == std::make_pair(3, -3));
    }

    SECTION("Line from (0, 0) to (-3, 3)") {
        auto result = bresenham_line(0, 0, -3, 3);
        REQUIRE(result.size() == 4);
        CHECK(result[0] == std::make_pair(0, 0));
        CHECK(result[1] == std::make_pair(-1, 1));
        CHECK(result[2] == std::make_pair(-2, 2));
        CHECK(result[3] == std::make_pair(-3, 3));
    }

    SECTION("Line from (0, 0) to (-3, -3)") {
        auto result = bresenham_line(0, 0, -3, -3);
        REQUIRE(result.size() == 4);
        CHECK(result[0] == std::make_pair(0, 0));
        CHECK(result[1] == std::make_pair(-1, -1));
        CHECK(result[2] == std::make_pair(-2, -2));
        CHECK(result[3] == std::make_pair(-3, -3));
    }

    SECTION("Horizontal line") {
        auto result = bresenham_line(0, 0, 5, 0);
        REQUIRE(result.size() == 6);
        for (int i = 0; i <= 5; ++i) {
            CHECK(result[i] == std::make_pair(i, 0));
        }
    }

    SECTION("Vertical line") {
        auto result = bresenham_line(0, 0, 0, 5);
        REQUIRE(result.size() == 6);
        for (int i = 0; i <= 5; ++i) {
            CHECK(result[i] == std::make_pair(0, i));
        }
    }
}