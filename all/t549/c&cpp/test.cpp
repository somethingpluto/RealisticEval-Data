const double k_B_over_keV = 8.617333262145e-5
TEST_CASE("TestGetTInLog10Kelvin", "[TemperatureConversion]") {
    SECTION("test_scalar_input_high_temperature") {
        double T_keV = 100.0;
        double expected_result = std::log10(T_keV / k_B_over_keV);
        REQUIRE(std::abs(get_T_in_log10_Kelvin(T_keV) - expected_result) < 1e-6);
    }

    SECTION("test_scalar_input_low_temperature") {
        double T_keV = 0.01;
        double expected_result = std::log10(T_keV / k_B_over_keV);
        REQUIRE(std::abs(get_T_in_log10_Kelvin(T_keV) - expected_result) < 1e-6);
    }

    SECTION("test_tuple_input_large_range") {
        std::tuple<double, double, double, double, double> T_keV = std::make_tuple(0.1, 1.0, 10.0, 100.0, 1000.0);
        auto expected_results = std::make_tuple(
            std::log10(std::get<0>(T_keV) / k_B_over_keV),
            std::log10(std::get<1>(T_keV) / k_B_over_keV),
            std::log10(std::get<2>(T_keV) / k_B_over_keV),
            std::log10(std::get<3>(T_keV) / k_B_over_keV),
            std::log10(std::get<4>(T_keV) / k_B_over_keV)
        );
        auto result = get_T_in_log10_Kelvin(T_keV);
        REQUIRE(result == expected_results);
    }

    SECTION("test_tuple_input_repeated_values") {
        std::tuple<double, double, double> T_keV = std::make_tuple(1.0, 1.0, 1.0);
        auto expected_results = std::make_tuple(
            std::log10(std::get<0>(T_keV) / k_B_over_keV),
            std::log10(std::get<1>(T_keV) / k_B_over_keV),
            std::log10(std::get<2>(T_keV) / k_B_over_keV)
        );
        auto result = get_T_in_log10_Kelvin(T_keV);
        REQUIRE(result == expected_results);
    }

    SECTION("test_scalar_input_non_integer") {
        double T_keV = 2.5;
        double expected_result = std::log10(T_keV / k_B_over_keV);
        REQUIRE(std::abs(get_T_in_log10_Kelvin(T_keV) - expected_result) < 1e-6);
    }

    SECTION("test_tuple_input_floating_point") {
        std::tuple<double, double, double> T_keV = std::make_tuple(1.5, 2.5, 3.5);
        auto expected_results = std::make_tuple(
            std::log10(std::get<0>(T_keV) / k_B_over_keV),
            std::log10(std::get<1>(T_keV) / k_B_over_keV),
            std::log10(std::get<2>(T_keV) / k_B_over_keV)
        );
        auto result = get_T_in_log10_Kelvin(T_keV);
        REQUIRE(result == expected_results);
    }

    SECTION("test_large_tuple_input") {
        std::vector<double> T_keV;
        for (double i = 1.0; i <= 1000.0; ++i) {
            T_keV.push_back(i);
        }
        std::tuple<double...> tuple_T_keV = std::make_tuple(T_keV.begin(), T_keV.end());
        auto expected_results = std::make_tuple(
            (std::log10(T_keV[0] / k_B_over_keV)),
            (std::log10(T_keV[1] / k_B_over_keV)),
            (std::log10(T_keV[2] / k_B_over_keV)),
            (std::log10(T_keV[3] / k_B_over_keV)),
            (std::log10(T_keV[4] / k_B_over_keV)),
            (std::log10(T_keV[5] / k_B_over_keV)),
            (std::log10(T_keV[6] / k_B_over_keV)),
            (std::log10(T_keV[7] / k_B_over_keV)),
            (std::log10(T_keV[8] / k_B_over_keV)),
            (std::log10(T_keV[9] / k_B_over_keV))
            // ... (more elements can be added here)
        );
        auto result = get_T_in_log10_Kelvin(tuple_T_keV);
        REQUIRE(result == expected_results);
    }
}