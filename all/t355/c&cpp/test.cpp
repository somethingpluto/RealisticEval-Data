TEST_CASE("Spatial Weight Calculation Tests") {

    SECTION("Zero Spatial Difference") {
        // When spatial difference is zero, weight should be 1
        float spatial_diff = 0.0f;
        float sigma_space = 1.0f; // arbitrary sigma value
        REQUIRE(spatialWeight(spatial_diff, sigma_space) == Approx(1.0f).epsilon(0.001));
    }

    SECTION("Positive Spatial Difference") {
        // A positive spatial difference with a reasonable sigma
        float spatial_diff = 2.0f;
        float sigma_space = 2.0f;
        float expected_weight = exp(-(spatial_diff * spatial_diff) / (2 * sigma_space * sigma_space));
        REQUIRE(spatialWeight(spatial_diff, sigma_space) == Approx(expected_weight).epsilon(0.001));
    }

    SECTION("Negative Spatial Difference") {
        // A negative spatial difference should yield the same weight as positive
        float spatial_diff = -2.0f;
        float sigma_space = 2.0f;
        float expected_weight = exp(-(spatial_diff * spatial_diff) / (2 * sigma_space * sigma_space));
        REQUIRE(spatialWeight(spatial_diff, sigma_space) == Approx(expected_weight).epsilon(0.001));
    }

    SECTION("Small Sigma Space") {
        // Test with a small sigma value
        float spatial_diff = 1.0f;
        float sigma_space = 0.1f;
        float expected_weight = exp(-(spatial_diff * spatial_diff) / (2 * sigma_space * sigma_space));
        REQUIRE(spatialWeight(spatial_diff, sigma_space) == Approx(expected_weight).epsilon(0.001));
    }

    SECTION("Large Sigma Space") {
        // Test with a large sigma value
        float spatial_diff = 1.0f;
        float sigma_space = 100.0f;
        float expected_weight = exp(-(spatial_diff * spatial_diff) / (2 * sigma_space * sigma_space));
        REQUIRE(spatialWeight(spatial_diff, sigma_space) == Approx(expected_weight).epsilon(0.001));
    }

}