TEST_CASE("TestAnswer") {
    
    SECTION("test_calculate_with_valid_input") {
        std::vector<int> values = {1, 2, 3, 4, 5};
        int period = 3;
        double expected = 4.0; // (3 + 4 + 5) / 3
        REQUIRE(calculate(values, period) == Approx(expected));
    }

    SECTION("test_calculate_with_all_same_values") {
        std::vector<int> values = {5, 5, 5, 5, 5};
        int period = 5;
        double expected = 5.0; // (5 + 5 + 5 + 5 + 5) / 5
        REQUIRE(calculate(values, period) == Approx(expected));
    }

    SECTION("test_calculate_with_single_value") {
        std::vector<int> values = {10};
        int period = 1;
        double expected = 10.0; // (10) / 1
        REQUIRE(calculate(values, period) == Approx(expected));
    }

    SECTION("test_calculate_with_insufficient_values") {
        std::vector<int> values = {1, 2};
        int period = 3;
        REQUIRE(std::isnan(calculate(values, period))); // Expecting NaN
    }

    SECTION("test_calculate_with_empty_list") {
        std::vector<int> values = {};
        int period = 1;
        REQUIRE(std::isnan(calculate(values, period))); // Expecting NaN
    }

    SECTION("test_calculate_with_negative_period") {
        std::vector<int> values = {1, 2, 3, 4, 5};
        int period = -1;
        REQUIRE(std::isnan(calculate(values, period))); // Expecting NaN
    }
}