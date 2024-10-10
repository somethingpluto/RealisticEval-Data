TEST_CASE("Calculate Euclidean Distance", "[calculateEuclideanDistance]") {
    SECTION("Two points with equal coordinates") {
        auto result = calculateEuclideanDistance({0.0f, 0.0f}, {0.0f, 0.0f});
        REQUIRE(result == Approx(0.0f));
    }

    SECTION("Two points on the x-axis") {
        auto result = calculateEuclideanDistance({1.0f, 0.0f}, {4.0f, 0.0f});
        REQUIRE(result == Approx(3.0f));
    }

    SECTION("Two points on the y-axis") {
        auto result = calculateEuclideanDistance({0.0f, 5.0f}, {0.0f, 8.0f});
        REQUIRE(result == Approx(3.0f));
    }

    SECTION("Two points in general position") {
        auto result = calculateEuclideanDistance({-2.0f, 3.0f}, {4.0f, -6.0f});
        REQUIRE(result == Approx(std::sqrt(77)).epsilon(0.01f));
    }
}