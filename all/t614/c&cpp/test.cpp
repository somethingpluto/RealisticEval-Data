TEST_CASE("TestCalculateAverageDifference") {
    
    SECTION("Positive integers") {
        std::vector<int> numbers = {10, 20, 30, 40};
        double result = calculate_average_difference(numbers);
        double expected = 10.0;
        REQUIRE(result == Approx(expected).epsilon(0.001)); // Using Approx for floating-point comparison
    }

    SECTION("Mixed positive and negative integers") {
        std::vector<int> numbers = {-10, 0, 10, 20};
        double result = calculate_average_difference(numbers);
        double expected = 10.0;
        REQUIRE(result == Approx(expected).epsilon(0.001));
    }

    SECTION("Same values") {
        std::vector<int> numbers = {5, 5, 5, 5};
        double result = calculate_average_difference(numbers);
        double expected = 0.0;
        REQUIRE(result == Approx(expected).epsilon(0.001));
    }

    SECTION("Single element") {
        std::vector<int> numbers = {100};
        double result = calculate_average_difference(numbers);
        double expected = 0.0; // Not enough data to calculate differences
        REQUIRE(result == Approx(expected).epsilon(0.001));
    }

    SECTION("Empty list") {
        std::vector<int> numbers = {};
        double result = calculate_average_difference(numbers);
        double expected = 0.0; // Not enough data to calculate differences
        REQUIRE(result == Approx(expected).epsilon(0.001));
    }
}