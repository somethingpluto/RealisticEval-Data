TEST_CASE("countNumbers") {
    SECTION("should return the correct count for a string with multiple numbers") {
        REQUIRE(countNumbers("There are 123 numbers in this string.") == 3); // '123' contains three numeric characters
    }

    SECTION("should return 0 for a string with no numbers") {
        REQUIRE(countNumbers("No numbers here!") == 0); // No numeric characters in 'No numbers here!'
    }

    SECTION("should return the correct count for a string with mixed characters") {
        REQUIRE(countNumbers("Room 101 and Room 102") == 6); // '101' and '102' together contain six numeric characters
    }

    SECTION("should return the correct count for a string with only numbers") {
        REQUIRE(countNumbers("1234567890") == 10); // '1234567890' contains ten numeric characters
    }

    SECTION("should return 0 for an empty string") {
        REQUIRE(countNumbers("") == 0); // An empty string contains no numeric characters
    }
}