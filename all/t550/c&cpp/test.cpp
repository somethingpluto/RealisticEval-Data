TEST_CASE("Test conversion of log10(K) to keV", "[convert_log10_K_to_keV]") {
    SECTION("Test conversion of a single scalar log10(K) value") {
        double T_log10_K = 3.0;
        double expected_result = std::pow(10, T_log10_K) * k_B_over_keV;
        REQUIRE(std::abs(convert_log10_K_to_keV(T_log10_K) - expected_result) < 1e-6);
    }

    SECTION("Test conversion of a tuple of log10(K) values") {
        std::tuple<double, double, double> T_log10_K = std::make_tuple(2.0, 3.0, 4.0);
        std::tuple<double, double, double> expected_results = std::make_tuple(
            std::pow(10, std::get<0>(T_log10_K)) * k_B_over_keV,
            std::pow(10, std::get<1>(T_log10_K)) * k_B_over_keV,
            std::pow(10, std::get<2>(T_log10_K)) * k_B_over_keV
        );
        auto result = convert_log10_K_to_keV(T_log10_K);
        REQUIRE(std::abs(std::get<0>(result) - std::get<0>(expected_results)) < 1e-6);
        REQUIRE(std::abs(std::get<1>(result) - std::get<1>(expected_results)) < 1e-6);
        REQUIRE(std::abs(std::get<2>(result) - std::get<2>(expected_results)) < 1e-6);
    }

    SECTION("Test conversion of log10(K) = 0") {
        double T_log10_K = 0.0;
        double expected_result = std::pow(10, T_log10_K) * k_B_over_keV;
        REQUIRE(std::abs(convert_log10_K_to_keV(T_log10_K) - expected_result) < 1e-6);
    }

    SECTION("Test conversion of a negative log10(K) value") {
        double T_log10_K = -1.0;
        double expected_result = std::pow(10, T_log10_K) * k_B_over_keV;
        REQUIRE(std::abs(convert_log10_K_to_keV(T_log10_K) - expected_result) < 1e-6);
    }

    SECTION("Test conversion of a large tuple of log10(K) values") {
        std::tuple<double, double, double, double, double> T_log10_K = std::make_tuple(1.0, 2.0, 3.0, 4.0, 5.0);
        std::tuple<double, double, double, double, double> expected_results = std::make_tuple(
            std::pow(10, std::get<0>(T_log10_K)) * k_B_over_keV,
            std::pow(10, std::get<1>(T_log10_K)) * k_B_over_keV,
            std::pow(10, std::get<2>(T_log10_K)) * k_B_over_keV,
            std::pow(10, std::get<3>(T_log10_K)) * k_B_over_keV,
            std::pow(10, std::get<4>(T_log10_K)) * k_B_over_keV
        );
        auto result = convert_log10_K_to_keV(T_log10_K);
        REQUIRE(std::abs(std::get<0>(result) - std::get<0>(expected_results)) < 1e-6);
        REQUIRE(std::abs(std::get<1>(result) - std::get<1>(expected_results)) < 1e-6);
        REQUIRE(std::abs(std::get<2>(result) - std::get<2>(expected_results)) < 1e-6);
        REQUIRE(std::abs(std::get<3>(result) - std::get<3>(expected_results)) < 1e-6);
        REQUIRE(std::abs(std::get<4>(result) - std::get<4>(expected_results)) < 1e-6);
    }

    SECTION("Test conversion of a large log10(K) value") {
        double T_log10_K = 10.0;
        double expected_result = std::pow(10, T_log10_K) * k_B_over_keV;
        REQUIRE(std::abs(convert_log10_K_to_keV(T_log10_K) - expected_result) < 1e-6);
    }

    SECTION("Test conversion with invalid input (string)") {
        // In C++, we cannot pass a string directly to the function, so we simulate this by passing an invalid type.
        // We use a lambda to capture the exception.
        REQUIRE_THROWS_AS((void)convert_log10_K_to_keV("invalid"), std::invalid_argument);
    }
}