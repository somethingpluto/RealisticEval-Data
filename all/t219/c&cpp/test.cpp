TEST_CASE("Check Dividend Variances", "[check_dividend_variances]") {
    vector<Record> records = {
        {"AAPL", "2023-10-05", 1.5},
        {"GOOGL", "2023-10-05", 2.0},
        {"MSFT", "2023-10-06", 1.0},
        {"AAPL", "2023-10-05", 1.8}
    };

    vector<Record> expected = {
        {"AAPL", "2023-10-05"}
    };

    vector<Record> result = check_dividend_variances(records);

    REQUIRE(result.size() == expected.size());
    for (size_t i = 0; i < result.size(); ++i) {
        REQUIRE(result[i].ticker == expected[i].ticker);
        REQUIRE(result[i].ex_dividend_date == expected[i].ex_dividend_date);
    }
}