TEST_CASE("isValidPortNumber") {
    SECTION("returns true for a valid port number in the middle of the range") {
        REQUIRE(isValidPortNumber(8080) == true);
    }

    SECTION("returns true for the lowest valid port number") {
        REQUIRE(isValidPortNumber(1) == true);
    }

    SECTION("returns true for the highest valid port number") {
        REQUIRE(isValidPortNumber(65535) == true);
    }

    SECTION("returns false for a port number below the valid range") {
        REQUIRE_THROWS_AS(isValidPortNumber(0), std::invalid_argument);
    }

    SECTION("returns false for a port number above the valid range") {
        REQUIRE_THROWS_AS(isValidPortNumber(65536), std::invalid_argument);
    }
}