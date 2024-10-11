TEST_CASE("test_intersecting_lines") {
    auto result = get_line_segment_intersection({{1, 1}, {4, 4}}, {{1, 4}, {4, 1}});
    REQUIRE(result.has_value());
    REQUIRE(result.value() == make_pair(2.5, 2.5));
}

TEST_CASE("test_parallel_lines") {
    auto result = get_line_segment_intersection({{1, 1}, {4, 4}}, {{2, 2}, {5, 5}});
    REQUIRE_FALSE(result.has_value());
}

TEST_CASE("test_no_intersection") {
    auto result = get_line_segment_intersection({{1, 1}, {2, 2}}, {{3, 3}, {4, 4}});
    REQUIRE_FALSE(result.has_value());
}

TEST_CASE("test_intersection_in_middle") {
    auto result = get_line_segment_intersection({{0, 0}, {4, 4}}, {{0, 4}, {4, 0}});
    REQUIRE(result.has_value());
    REQUIRE(abs(result->first - 2.0) < 1e-7);
    REQUIRE(abs(result->second - 2.0) < 1e-7);
}

TEST_CASE("test_identical_segments") {
    auto result = get_line_segment_intersection({{1, 1}, {4, 4}}, {{1, 1}, {4, 4}});
    REQUIRE_FALSE(result.has_value());
}