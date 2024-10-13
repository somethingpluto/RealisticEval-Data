TEST_CASE("Test Line Segment Intersection") {
    SECTION("Intersection") {
        auto seg1 = std::make_pair(std::make_pair(1.0, 1.0), std::make_pair(4.0, 4.0));
        auto seg2 = std::make_pair(std::make_pair(1.0, 4.0), std::make_pair(4.0, 1.0));
        auto expected = std::make_pair(2.5, 2.5);
        auto result = getLineSegmentIntersection(seg1, seg2);
        REQUIRE(result == expected);
    }

    SECTION("No Intersection") {
        auto seg1 = std::make_pair(std::make_pair(1.0, 1.0), std::make_pair(2.0, 2.0));
        auto seg2 = std::make_pair(std::make_pair(3.0, 3.0), std::make_pair(4.0, 4.0));
        auto result = getLineSegmentIntersection(seg1, seg2);
        REQUIRE(result == true); // True indicates no intersection
    }

    SECTION("Parallel Segments") {
        auto seg1 = std::make_pair(std::make_pair(1.0, 1.0), std::make_pair(2.0, 2.0));
        auto seg2 = std::make_pair(std::make_pair(1.0, 2.0), std::make_pair(2.0, 3.0));
        auto result = getLineSegmentIntersection(seg1, seg2);
        REQUIRE(result == true); // True indicates no intersection
    }

    SECTION("No Intersection Due to Offset") {
        auto seg1 = std::make_pair(std::make_pair(1.0, 1.0), std::make_pair(3.0, 3.0));
        auto seg2 = std::make_pair(std::make_pair(3.0, 2.0), std::make_pair(4.0, 2.0));
        auto result = getLineSegmentIntersection(seg1, seg2);
        REQUIRE(result == true); // True indicates no intersection
    }

    SECTION("Intersection with Large Coordinates") {
        auto seg1 = std::make_pair(std::make_pair(1000.0, 1000.0), std::make_pair(2000.0, 2000.0));
        auto seg2 = std::make_pair(std::make_pair(1000.0, 2000.0), std::make_pair(2000.0, 1000.0));
        auto expected = std::make_pair(1500.0, 1500.0);
        auto result = getLineSegmentIntersection(seg1, seg2);
        REQUIRE(result == expected);
    }
}