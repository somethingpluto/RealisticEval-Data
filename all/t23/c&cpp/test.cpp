TEST_CASE("Test Line Segment Intersection", "[intersection]") {
    
    SECTION("Intersection of two segments") {
        std::pair<std::tuple<float, float>, std::tuple<float, float>> seg1{{1.0, 1.0}, {4.0, 4.0}};
        std::pair<std::tuple<float, float>, std::tuple<float, float>> seg2{{1.0, 4.0}, {4.0, 1.0}};
        auto result = check_segments_intersection(seg1, seg2);
        REQUIRE(result == std::make_tuple(2.5f, 2.5f));
    }

    SECTION("No intersection") {
        std::pair<std::tuple<float, float>, std::tuple<float, float>> seg1{{1.0, 1.0}, {2.0, 2.0}};
        std::pair<std::tuple<float, float>, std::tuple<float, float>> seg2{{3.0, 3.0}, {4.0, 4.0}};
        auto result = check_segments_intersection(seg1, seg2);
        REQUIRE(result == std::nullopt);  // Assumes the function returns std::optional<std::tuple<float, float>> for no intersection
    }

    SECTION("Parallel segments") {
        std::pair<std::tuple<float, float>, std::tuple<float, float>> seg1{{1.0, 1.0}, {2.0, 2.0}};
        std::pair<std::tuple<float, float>, std::tuple<float, float>> seg2{{1.0, 2.0}, {2.0, 3.0}};
        auto result = check_segments_intersection(seg1, seg2);
        REQUIRE(result == std::nullopt);  // Parallel segments do not intersect
    }

    SECTION("No intersection due to offset") {
        std::pair<std::tuple<float, float>, std::tuple<float, float>> seg1{{1.0, 1.0}, {3.0, 3.0}};
        std::pair<std::tuple<float, float>, std::tuple<float, float>> seg2{{3.0, 2.0}, {4.0, 2.0}};
        auto result = check_segments_intersection(seg1, seg2);
        REQUIRE(result == std::nullopt);  // Segments don't intersect because they're offset
    }

    SECTION("Intersection with large coordinates") {
        std::pair<std::tuple<float, float>, std::tuple<float, float>> seg1{{1000.0, 1000.0}, {2000.0, 2000.0}};
        std::pair<std::tuple<float, float>, std::tuple<float, float>> seg2{{1000.0, 2000.0}, {2000.0, 1000.0}};
        auto result = check_segments_intersection(seg1, seg2);
        REQUIRE(result == std::make_tuple(1500.0f, 1500.0f));  // Intersection should be at (1500.0, 1500.0)
    }
}