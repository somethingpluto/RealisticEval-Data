// Test cases for gaussianWeight function
TEST_CASE("Gaussian Weight Calculation Tests") {

    SECTION("Zero Intensity Difference") {
        // When intensity difference is zero, weight should be 1
        float intensity_diff = 0.0f;
        float sigma_color = 1.0f; // arbitrary sigma value
        REQUIRE(gaussianWeight(intensity_diff, sigma_color) == Approx(1.0f).epsilon(0.001));
    }

    SECTION("Positive Intensity Difference") {
        // A positive intensity difference with a reasonable sigma
        float intensity_diff = 2.0f;
        float sigma_color = 2.0f;
        float expected_weight = exp(-(intensity_diff * intensity_diff) / (2 * sigma_color * sigma_color));
        REQUIRE(gaussianWeight(intensity_diff, sigma_color) == Approx(expected_weight).epsilon(0.001));
    }

    SECTION("Negative Intensity Difference") {
        // A negative intensity difference should yield the same weight as positive
        float intensity_diff = -2.0f;
        float sigma_color = 2.0f;
        float expected_weight = exp(-(intensity_diff * intensity_diff) / (2 * sigma_color * sigma_color));
        REQUIRE(gaussianWeight(intensity_diff, sigma_color) == Approx(expected_weight).epsilon(0.001));
    }

    SECTION("Small Sigma Color") {
        // Test with a small sigma value
        float intensity_diff = 1.0f;
        float sigma_color = 0.1f;
        float expected_weight = exp(-(intensity_diff * intensity_diff) / (2 * sigma_color * sigma_color));
        REQUIRE(gaussianWeight(intensity_diff, sigma_color) == Approx(expected_weight).epsilon(0.001));
    }

    SECTION("Large Sigma Color") {
        // Test with a large sigma value
        float intensity_diff = 1.0f;
        float sigma_color = 100.0f;
        float expected_weight = exp(-(intensity_diff * intensity_diff) / (2 * sigma_color * sigma_color));
        REQUIRE(gaussianWeight(intensity_diff, sigma_color) == Approx(expected_weight).epsilon(0.001));
    }
}