TEST_CASE("Test basic functionality") {
    // Basic logic functionality test
    auto point1 = std::make_tuple(0.0f, 0.0f);
    auto point2 = std::make_tuple(3.0f, 4.0f);
    float expected_distance = 5.0f;

    REQUIRE(calculate_euclidean_distance(point1, point2) == Approx(expected_distance));
}

TEST_CASE("Test with negative coordinates") {
    // Test with negative coordinates
    auto point1 = std::make_tuple(-1.0f, -1.0f);
    auto point2 = std::make_tuple(-4.0f, -5.0f);
    float expected_distance = 5.0f;

    REQUIRE(calculate_euclidean_distance(point1, point2) == Approx(expected_distance));
}

TEST_CASE("Test zero distance") {
    // Boundary test: points are the same
    auto point1 = std::make_tuple(2.0f, 3.0f);
    auto point2 = std::make_tuple(2.0f, 3.0f);
    float expected_distance = 0.0f;

    REQUIRE(calculate_euclidean_distance(point1, point2) == Approx(expected_distance));
}

TEST_CASE("Test large coordinates") {
    // Boundary test: large coordinates
    auto point1 = std::make_tuple(1e6f, 1e6f);
    auto point2 = std::make_tuple(1e6f + 3.0f, 1e6f + 4.0f);
    float expected_distance = 5.0f;

    REQUIRE(calculate_euclidean_distance(point1, point2) == Approx(expected_distance));
}

TEST_CASE("Test invalid input") {
    // Exception handling test: invalid input (non-tuple)
    REQUIRE_THROWS_AS(calculate_euclidean_distance(std::make_tuple("invalid", 0.0f), std::make_tuple(0.0f, 0.0f)), std::invalid_argument);
}
