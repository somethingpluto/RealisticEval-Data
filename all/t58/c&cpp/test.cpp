bool isclose(double a, double b, double rel_tol = 1e-9, double abs_tol = 0.0) {
    return std::abs(a - b) <= std::max(rel_tol * std::max(std::abs(a), std::abs(b)), abs_tol);
}

// Test suite for the probability_of_red_balls function
TEST_CASE("Test probability_of_red_balls", "[probability_of_red_balls]") {
    SECTION("Test with half red balls") {
        // Scenario where half of the drawn balls are expected to be red
        double result = probability_of_red_balls(7, 10, 10);
        double expected_result = 0.0542635;  // Manually calculated or from another tool
        REQUIRE(isclose(result, expected_result));
    }

    SECTION("Test with some red balls") {
        // Scenario with some red balls in the jar, expecting a few red draws
        double result = probability_of_red_balls(5, 5, 10);
        double expected_result = 0.00371398;  // Manually calculated or from another tool
        REQUIRE(isclose(result, expected_result));
    }

    SECTION("Test with extreme case") {
        // Extreme scenario where the probability is low for the chosen n
        double result = probability_of_red_balls(15, 1, 99);
        double expected_result = 1.01168e-10;  // Manually calculated or from another tool
        REQUIRE(isclose(result, expected_result));
    }
}