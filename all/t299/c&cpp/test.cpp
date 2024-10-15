TEST_CASE("calculateAge") {
    SECTION("Birthday today, should be 24 years old") {
        REQUIRE(calculateAge("2000-08-23") == "2000-08-23 (24)");
    }

    SECTION("Birthday has passed this year, should be 34 years old") {
        REQUIRE(calculateAge("1990-01-15") == "1990-01-15 (34)");
    }

    SECTION("Birthday at the end of the year, should be 38 years old") {
        REQUIRE(calculateAge("1985-12-31") == "1985-12-31 (38)");
    }

    SECTION("Recently turned 1 year old this year") {
        REQUIRE(calculateAge("2023-05-05") == "2023-05-05 (1)");
    }

    SECTION("Invalid date input should return an empty string") {
        REQUIRE(calculateAge("invalid-date") == "");
    }
}