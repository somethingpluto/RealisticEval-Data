TEST_CASE("Test checkDividendVariances function", "[checkDividendVariances]") {
    SECTION("No inconsistencies") {
        std::vector<std::tuple<std::string, std::string, int>> records = {
            {"AAPL", "2023-09-01", 22},
            {"AAPL", "2023-09-01", 22},
            {"MSFT", "2023-09-01", 56},
            {"GOOG", "2023-09-02", 0}
        };
        std::vector<std::pair<std::string, std::string>> expected_output = {};
        REQUIRE(checkDividendVariances(records) == expected_output);
    }

    SECTION("One inconsistency") {
        std::vector<std::tuple<std::string, std::string, int>> records = {
            {"AAPL", "2023-09-01", 22},
            {"AAPL", "2023-09-01", 23},  // Different amount
            {"MSFT", "2023-09-01", 56},
            {"GOOG", "2023-09-02", 0}
        };
        std::vector<std::pair<std::string, std::string>> expected_output = {{"AAPL", "2023-09-01"}};
        REQUIRE(checkDividendVariances(records) == expected_output);
    }

    SECTION("Multiple inconsistencies") {
        std::vector<std::tuple<std::string, std::string, int>> records = {
            {"AAPL", "2023-09-01", 22},
            {"AAPL", "2023-09-01", 23},  // Different amount
            {"MSFT", "2023-09-01", 56},
            {"MSFT", "2023-09-01", 60},  // Different amount
            {"GOOG", "2023-09-02", 0},
            {"TSLA", "2023-09-03", 10},
            {"TSLA", "2023-09-03", 10},  // Same amount, no inconsistency
            {"TSLA", "2023-09-03", 15}  // Different amount
        };
        std::vector<std::pair<std::string, std::string>> expected_output = {
            {"AAPL", "2023-09-01"},
            {"MSFT", "2023-09-01"},
            {"TSLA", "2023-09-03"}
        };
        REQUIRE(checkDividendVariances(records) == expected_output);
    }

    SECTION("Single record") {
        std::vector<std::tuple<std::string, std::string, int>> records = {
            {"AAPL", "2023-09-01", 22}
        };
        std::vector<std::pair<std::string, std::string>> expected_output = {};
        REQUIRE(checkDividendVariances(records) == expected_output);
    }

    SECTION("Empty list") {
        std::vector<std::tuple<std::string, std::string, int>> records = {};
        std::vector<std::pair<std::string, std::string>> expected_output = {};
        REQUIRE(checkDividendVariances(records) == expected_output);
    }
}