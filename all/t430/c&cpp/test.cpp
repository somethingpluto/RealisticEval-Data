TEST_CASE("Test Intersect Vertically", "[intersect_vertically]") {
    SECTION("Test with overlapping rectangles") {
        auto rect1 = std::make_tuple(0, 0, 2, 2);
        auto rect2 = std::make_tuple(1, 1, 3, 3);
        REQUIRE(intersect_vertically(rect1, rect2));
    }

    SECTION("Test with overlapping rectangles") {
        auto rect1 = std::make_tuple(-1, -1, 1, 1);
        auto rect2 = std::make_tuple(0, 0, 2, 2);
        REQUIRE(intersect_vertically(rect1, rect2));
    }

    SECTION("Test case where rectangles partially overlap vertically") {
        auto rect1 = std::make_tuple(0, 1, 2, 4);
        auto rect2 = std::make_tuple(1, 0, 3, 2);
        REQUIRE(intersect_vertically(rect1, rect2));
    }

    SECTION("Test case where rectangles are identical") {
        auto rect1 = std::make_tuple(0, 0, 2, 2);
        auto rect2 = std::make_tuple(0, 0, 2, 2);
        REQUIRE(intersect_vertically(rect1, rect2));
    }

    SECTION("Test case where one rectangle is completely inside the other") {
        auto rect1 = std::make_tuple(0, 0, 4, 4);
        auto rect2 = std::make_tuple(1, 1, 2, 2);
        REQUIRE(intersect_vertically(rect1, rect2));
    }
}