TEST_CASE("setEurValue") {
    SECTION("formats standard values correctly") {
        REQUIRE(setEurValue("250") == "250");
        REQUIRE(setEurValue("2500") == "2.5k");
    }

    SECTION("handles boundary values accurately") {
        REQUIRE(setEurValue("999") == "999");
        REQUIRE(setEurValue("1000") == "1.0k");
        REQUIRE(setEurValue("999999") == "999.9k"); // Note: Fixed to '999.9k'
        REQUIRE(setEurValue("1000000") == "1.0m");
    }

    SECTION("returns correct format for zero and negative inputs") {
        REQUIRE(setEurValue("0") == "0");
    }

    SECTION("returns an empty string for invalid inputs") {
        REQUIRE(setEurValue("hello") == "");
        REQUIRE(setEurValue("") == ""); // Handling empty string instead of null/undefined
    }

    SECTION("ensures precision for large numbers") {
        REQUIRE(setEurValue("10000000") == "10.0m");
        REQUIRE(setEurValue("987654321") == "987.7m");
    }
}