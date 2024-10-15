TEST_CASE("calculateAge", "[age]") {
    SECTION("calculates age correctly for a birth date in the past") {
        REQUIRE(calculateAge("2000-01-01") == (std::time(0) / (365.25 * 24 * 60 * 60)) - 2000);
    }

    SECTION("calculates age correctly for a birth date in the long past") {
        REQUIRE(calculateAge("1000-01-01") == (std::time(0) / (365.25 * 24 * 60 * 60)) - 1000);
    }

    SECTION("calculates age correctly for a birth date today") {
        std::time_t now = std::time(0);
        std::tm* today = std::localtime(&now);
        std::ostringstream oss;
        oss << std::put_time(today, "%Y-%m-%d");
        REQUIRE(calculateAge(oss.str()) == 0);
    }

    SECTION("calculates age correctly for a person born yesterday") {
        std::time_t now = std::time(0);
        std::tm* yesterday = std::localtime(&now);
        yesterday->tm_mday--; // Set to yesterday
        std::mktime(yesterday); // Normalize the structure
        std::ostringstream oss;
        oss << std::put_time(yesterday, "%Y-%m-%d");
        REQUIRE(calculateAge(oss.str()) == 0);
    }
}