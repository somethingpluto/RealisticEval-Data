TEST_CASE("Test squared Euclidean distance calculations", "[squared_euclidean_distance]") {
    SECTION("Test standard vectors") {
        std::vector<int> vec1 = {1, 2, 3};
        std::vector<int> vec2 = {4, 5, 6};
        double expected_result = 27.0;  // (3^2 + 3^2 + 3^2)
        double result = squared_euclidean_distance(vec1, vec2);
        REQUIRE(result == Approx(expected_result));
    }

    SECTION("Test vectors with zeros") {
        std::vector<int> vec1 = {0, 0, 0};
        std::vector<int> vec2 = {0, 0, 0};
        double expected_result = 0.0;
        double result = squared_euclidean_distance(vec1, vec2);
        REQUIRE(result == Approx(expected_result));
    }

    SECTION("Test vectors with negative values") {
        std::vector<int> vec1 = {-1, -2, -3};
        std::vector<int> vec2 = {-4, -5, -6};
        double expected_result = 27.0;  // (3^2 + 3^2 + 3^2)
        double result = squared_euclidean_distance(vec1, vec2);
        REQUIRE(result == Approx(expected_result));
    }

    SECTION("Test single element vectors") {
        std::vector<int> vec1 = {5};
        std::vector<int> vec2 = {-5};
        double expected_result = 100.0;  // (10^2)
        double result = squared_euclidean_distance(vec1, vec2);
        REQUIRE(result == Approx(expected_result));
    }
}