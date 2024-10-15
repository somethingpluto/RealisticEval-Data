TEST_CASE("formatCurrency function tests") {
    SECTION("should format currency in US dollars") {
        double value = 1234.56;
        std::string currencyCode = "USD";
        std::string locale = "en-US";
        std::string expectedOutput = "$1,234.56"; // Expected format for USD
        REQUIRE(formatCurrency(value, currencyCode, locale) == expectedOutput);
    }

    SECTION("should format currency in Euro") {
        double value = 1234.56;
        std::string currencyCode = "EUR";
        std::string locale = "en-US";
        std::string expectedOutput = "€1,234.56"; // Expected format for EUR
        REQUIRE(formatCurrency(value, currencyCode, locale) == expectedOutput);
    }

    SECTION("should format currency in British Pound") {
        double value = 1234.56;
        std::string currencyCode = "GBP";
        std::string locale = "en-GB";
        std::string expectedOutput = "£1,234.56"; // Expected format for GBP
        REQUIRE(formatCurrency(value, currencyCode, locale) == expectedOutput);
    }

    SECTION("should format currency with a negative value") {
        double value = -1234.56;
        std::string currencyCode = "USD";
        std::string locale = "en-US";
        std::string expectedOutput = "-$1,234.56"; // Expected format for negative USD
        REQUIRE(formatCurrency(value, currencyCode, locale) == expectedOutput);
    }

    SECTION("should handle zero value correctly") {
        double value = 0;
        std::string currencyCode = "JPY";
        std::string locale = "en-JP";
        std::string expectedOutput = "¥0"; // Expected format for JPY (no decimals)
        REQUIRE(formatCurrency(value, currencyCode, locale) == expectedOutput);
    }
}