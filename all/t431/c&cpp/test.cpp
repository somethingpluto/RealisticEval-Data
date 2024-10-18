TEST_CASE("Test intersect_horizontally", "[intersect_horizontally]") {
    SECTION("Test with overlapping rectangles") {
        auto rect1 = std::make_tuple(0, 0, 2, 2);
        auto rect2 = std::make_tuple(1, 1, 3, 3);
        REQUIRE(intersect_horizontally(rect1, rect2));
    }

    SECTION("Test with rectangles touching at a point (not overlapping)") {
        auto rect1 = std::make_tuple(0, 0, 1, 1);
        auto rect2 = std::make_tuple(1, 1, 2, 2);
        REQUIRE(intersect_horizontally(rect1, rect2));
    }

    SECTION("Test with adjacent rectangles (no overlap)") {
        auto rect1 = std::make_tuple(0, 0, 2, 2);
        auto rect2 = std::make_tuple(2, 0, 3, 3);
        REQUIRE(intersect_horizontally(rect1, rect2));
    }

    SECTION("Test with one rectangle fully inside another") {
        auto rect1 = std::make_tuple(1, 1, 4, 4);
        auto rect2 = std::make_tuple(2, 2, 3, 3);
        REQUIRE(intersect_horizontally(rect1, rect2));
    }

    SECTION("Test with overlapping rectangles") {
        auto rect1 = std::make_tuple(-1, -1, 1, 1);
        auto rect2 = std::make_tuple(0, 0, 2, 2);
        REQUIRE(intersect_horizontally(rect1, rect2));
    }
}
